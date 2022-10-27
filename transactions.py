import obp_python as obp
from obp_client import client
from banks import get_bank_id_from_str
import constants as c
from accounts import check_account_exists


transactions = obp.TransactionRequestApi(client)
historical_transactions = obp.TransactionApi(client)
counterparties = obp.CounterpartyApi(client)

def get_from_and_to_account_for_transaction(row):
	# check which account exists
	debitor_bank_id = row[c.DEBTOR_BANK_ROUTING_ADDRESS].value
	debitor_routing_scheme = row[c.DEBTOR_ACCOUNT_ROUTING_SCHEME].value
	debitor_routing_address = row[c.DEBTOR_ACCOUNT_ROUTING_ADDRESS].value
	creditor_bank_id = row[c.CREDITOR_BANK_ROUTING_ADDRESS].value
	creditor_routing_scheme = row[c.CREDITOR_ACCOUNT_ROUTING_SCHEME].value
	creditor_routing_address = row[c.CREDITOR_ACCOUNT_ROUTING_ADDRESS].value

	debitor_account_id = check_account_exists(debitor_bank_id, debitor_routing_scheme, debitor_routing_address)
	creditor_account_id = check_account_exists(creditor_bank_id, creditor_routing_scheme, creditor_routing_address)
	if debitor_account_id:
		from_account = obp.HistoricalTransactionAccountJsonV310(
			bank_id=debitor_bank_id, account_id=debitor_account_id
		)
	else:
		from_account = obp.HistoricalTransactionAccountJsonV310(
			counterparty_id=''
		)
	if creditor_account_id:
		to_account = obp.HistoricalTransactionAccountJsonV310(
			bank_id=creditor_bank_id, account_id=creditor_account_id
		)
	else:
		to_account = obp.HistoricalTransactionAccountJsonV310(
			counterparty_id=''
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


def create_transaction_from_row(row):
	body = get_create_transaction_request_body(row)

	res = transactions.save_historical_transaction(
		body=body
	)
	return res


