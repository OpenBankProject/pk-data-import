from obp_client import logger, client, token, obp_host
import requests
import obp_python as obp
from obp_python.rest import ApiException

counterparties = obp.CounterpartyApi(client)

def get_counterparty(bank_id, account_id, counterparty_name):
	headers = {
		'Content-Type': 'application/json',
		'Authorization': f'DirectLogin token={token}'
	}

	url = f'{obp_host}/obp/v5.0.0/management/banks/{bank_id}/accounts/{account_id}/owner/counterparty-names/{counterparty_name}'
	req = requests.get(url, headers=headers)
	return req
def get_or_create_counterparty(counterparty_name, account_id, bank_id):
	try:
		res = get_counterparty(bank_id=bank_id, account_id=account_id, counterparty_name=counterparty_name)
		if res.status_code == 404:
			logger.debug(f'counterparty {counterparty_name} does not exist, creating now')
		logger.debug(f'Counterparty exists: {counterparty_name}')
		return res.json()["counterparty_id"]
	except Exception as e:
		logger.exception(f'get or create counterparty broke: {e}')

