from obp_client import logger, client, token, obp_host
import requests
import obp_python as obp

counterparty_api = obp.CounterpartyApi(client)


class MinimalCounterparty:
	def __init__(
			self,
			name,
			bank_routing_scheme,
			bank_routing_address,
			account_routing_scheme,
			account_routing_address,
			currency):
		self.name = name
		self.bank_routing_scheme = bank_routing_scheme
		self.bank_routing_address = bank_routing_address
		self.account_routing_scheme = account_routing_scheme
		self.account_routing_address = account_routing_address
		self.currency = currency


def get_counterparty(bank_id, account_id, counterparty_name):
	headers = {
		'Content-Type': 'application/json',
		'Authorization': f'DirectLogin token={token}'
	}

	url = f'{obp_host}/obp/v5.0.0/management/banks/{bank_id}/accounts/{account_id}/owner/counterparty-names/{counterparty_name}'
	req = requests.get(url, headers=headers)
	return req


def create_counterparty(minimal_counterparty: MinimalCounterparty, account_id, bank_id):
	body = obp.PostCounterpartyJson400(
		other_account_routing_address=minimal_counterparty.account_routing_address,
		other_account_routing_scheme=minimal_counterparty.account_routing_scheme,
		name=minimal_counterparty.name,
		other_account_secondary_routing_address='',
		is_beneficiary=True,
		description='',
		other_branch_routing_scheme='',
		other_branch_routing_address='',
		bespoke=[],
		other_bank_routing_scheme=minimal_counterparty.bank_routing_scheme,
		currency=minimal_counterparty.currency,
		other_bank_routing_address=minimal_counterparty.bank_routing_address,
		other_account_secondary_routing_scheme=''
	)
	res = counterparty_api.create_counterparty(
		body=body,
		view_id='owner',
		account_id=account_id,
		bank_id=bank_id
	)
	return res.counterparty_id


def get_or_create_counterparty(minimal_counter_party, account_id, bank_id):
	try:
		res = get_counterparty(bank_id=bank_id, account_id=account_id, counterparty_name=minimal_counter_party.name)
		if res.status_code >= 400:
			logger.debug(f'counterparty {minimal_counter_party.name} does not exist, creating now')
			return create_counterparty(minimal_counter_party, account_id, bank_id)
		logger.debug(f'Counterparty {minimal_counter_party.name} exists: {res.text}')
		return res.json()["counterparty_id"]
	except Exception as e:
		logger.exception(f'get or create counterparty broke: {e}')

