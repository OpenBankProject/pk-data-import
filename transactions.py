import obp_python as obp
from obp_client import client, logger
from banks import get_bank_id_from_str
import constants as c
from accounts import check_account_exists
from counterparties import get_or_create_counterparty, MinimalCounterparty
from json import loads

transaction_requests = obp.TransactionRequestApi(client)
transactions = obp.TransactionApi(client)
historical_transactions = obp.TransactionApi(client)
counterparties = obp.CounterpartyApi(client)


def get_from_and_to_account_for_transaction(row):
	debtor = MinimalCounterparty(
		name=row[c.DEBTOR_LEGAL_NAME].value,
		bank_routing_scheme=row[c.DEBTOR_BANK_ROUTING_SCHEME].value,
		bank_routing_address=get_bank_id_from_str(row[c.DEBTOR_BANK_ROUTING_ADDRESS].value),
		account_routing_scheme=row[c.DEBTOR_ACCOUNT_ROUTING_SCHEME].value,
		account_routing_address=row[c.DEBTOR_ACCOUNT_ROUTING_ADDRESS].value,
		currency=row[c.TRANSACTIONS_CURRENCY].value
	)
	creditor = MinimalCounterparty(
			name=row[c.CREDITOR_LEGAL_NAME].value,
			bank_routing_scheme=row[c.CREDITOR_BANK_ROUTING_SCHEME].value,
			bank_routing_address=get_bank_id_from_str(row[c.CREDITOR_BANK_ROUTING_ADDRESS].value),
			account_routing_scheme=row[c.CREDITOR_ACCOUNT_ROUTING_SCHEME].value,
			account_routing_address=row[c.CREDITOR_ACCOUNT_ROUTING_ADDRESS].value,
			currency=row[c.TRANSACTIONS_CURRENCY].value
	)
	debtor_account_id = check_account_exists(
		debtor.bank_routing_address,
		debtor.account_routing_scheme,
		debtor.account_routing_address
	)
	creditor_account_id = check_account_exists(
		creditor.bank_routing_address,
		creditor.account_routing_scheme,
		creditor.account_routing_address
	)
	if debtor_account_id:
		from_account = obp.HistoricalTransactionAccountJsonV310(
			bank_id=debtor.bank_routing_address, account_id=debtor_account_id
		)
	else:
		# At least one obp account has to exist!
		if not creditor_account_id:
			return None, None
		from_account = obp.HistoricalTransactionAccountJsonV310(
			counterparty_id=get_or_create_counterparty(debtor, creditor_account_id, creditor.bank_routing_address)
		)
	if creditor_account_id:
		to_account = obp.HistoricalTransactionAccountJsonV310(
			bank_id=creditor.bank_routing_address, account_id=creditor_account_id
		)
	else:
		to_account = obp.HistoricalTransactionAccountJsonV310(
			counterparty_id=get_or_create_counterparty(creditor, debtor_account_id, debtor.bank_routing_address)
		)
	return from_account, to_account


def get_create_transaction_request_body(row):
	from_account, to_account = get_from_and_to_account_for_transaction(row)
	value = obp.AmountOfMoneyJsonV121(
		currency=row[c.TRANSACTIONS_CURRENCY].value,
		amount=row[c.AMOUNT].value
	)
	body =obp.PostHistoricalTransactionJson(
		to=to_account,
		_from=from_account,
		completed=row[c.VALUE_DATE].value,
		posted=row[c.BOOKED_DATE].value,
		type="SANDBOX_TAN",
		charge_policy='',
		value=value,
		description=row[c.DESCRIPTION].value
	)
	return body


def create_transaction_from_row(row) -> obp.PostHistoricalTransactionResponseJson:
	body = get_create_transaction_request_body(row)

	res = transaction_requests.save_historical_transaction(
		body=body
	)
	return res


def create_transaction_attributes(attributes_list, transaction_id, account_id, bank_id):
	try:
		attributes_dict = loads(attributes_list)
		for k, v in attributes_dict.items():
			body = obp.TransactionAttributeJsonV400(
				name=k,
				type='STRING',
				value=v
			)
			transactions.create_transaction_attribute(
				body=body,
				transaction_id=transaction_id,
				account_id=account_id,
				bank_id=bank_id
			)
	except Exception as e:
		logger.exception(f'could not create transaction attributes: {e}')


def create_transaction_with_attributes_from_row(row):
	transaction = create_transaction_from_row(row)
	if transaction.to.account_id:
		account_id = transaction.to.account_id
		bank_id = transaction.to.bank_id
	else:
		account_id = transaction._from.account_id
		bank_id = transaction._from.bank_id
	create_transaction_attributes(
		row[c.TRANSACTION_ATTRIBUTES_LIST].value,
		transaction.transaction_id,
		account_id,
		bank_id
		)
	return transaction
