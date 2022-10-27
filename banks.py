import obp_python as obp
from obp_client import client, logger
import constants as c


banks = obp.BankApi(client)


def get_bank_id_from_str(bank_id_str):
	return bank_id_str.strip().replace(' ', '_')


def create_bank_request_body_from_row(row):
	try:
		bank_routing = obp.BankRoutingJsonV121(
			scheme=row[c.BANKS_BANK_ROUTING_SCHEME].value.strip(),
			address=row[c.BANKS_BANK_ROUTING_ADDRESS].value.strip()
		)
	except Exception as e:
		logger.exception(f'Could not create bank_routing for row {row[0].row}: {e}')
		return None
	if row[c.BANK_CODE].value:
		bank_code = row[c.BANK_CODE].value.strip()
	else:
		bank_code = None
	if row[c.LOGO].value:
		logo = row[c.LOGO].value.strip()
	else:
		logo = None
	if row[c.WEBSITE].value:
		website = row[c.WEBSITE].value.strip()
	else:
		website = None
	# those attributes will be ignored on obp side
	attributes = None
	try:
		body = obp.PostBankJson500(
			id=get_bank_id_from_str(row[c.BANK_ID].value),
			bank_routings=[bank_routing],
			full_name=row[c.FULL_NAME].value.strip(),
			bank_code=bank_code,
			logo=logo,
			website=website,
			attributes=attributes
		)
	except Exception as e:
		logger.exception(f'Could not create create_bank request body for row {row[0].row}: {e}')
		return None
	return body


def create_bank_from_row(row):
	body = create_bank_request_body_from_row(row)
	try:
		res = banks.create_bank(body=body)
		return res
	except Exception as e:
		logger.exception(f'Could not upload bank data for row {row[0].row}: {e}')

