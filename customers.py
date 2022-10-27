import obp_python as obp
from obp_client import client, configuration, logger
import constants as c
from banks import get_bank_id_from_str
from json import loads
customers = obp.CustomerApi(client)


def create_customer_attributes(attributes_list, customer_id, bank_id):
	try:
		attributes_dict = loads(attributes_list)
		for k, v in attributes_dict.items():
			body = obp.CustomerAttributeJsonV400(
				name=k,
				type='STRING',
				value=v
			)
			customers.create_customer_attribute(
				body=body,
				customer_id=customer_id,
				bank_id=bank_id
			)
	except Exception as e:
		logger.exception(f'could not create customer attributes: {e}')


def get_create_customer_request_body_from_row(row):
	if row[c.MOBILE_PHONE_NUMBER].value:
		mobile_phone_number = row[c.MOBILE_PHONE_NUMBER].value
	else:
		mobile_phone_number = ''
	body = obp.PostCustomerJsonV500(
		legal_name=row[c.LEGAL_NAME].value,
		name_suffix=row[c.NAME_SUFFIX].value,
		email=row[c.EMAIL].value,
		mobile_phone_number=mobile_phone_number,
		branch_id=row[c.BRANCH_ID].value,
		face_image=None,
		date_of_birth=row[c.DATE_OF_BIRTH].value,
		title=row[c.TITLE].value,
		_configuration=configuration
	)
	customer_number = row[c.CUSTOMER_NUMBER].value
	return body


def create_customer_from_row(row):
	bank_id = get_bank_id_from_str(row[c.BANK_ID].value)
	customer_nr = row[c.CUSTOMER_NUMBER].value
	body= get_create_customer_request_body_from_row(row)
	res = customers.create_customer(
		body=body, bank_id=bank_id,
	)
	try:
		customer_id = res.customer_id
		create_customer_attributes(row[c.CUSTOMER_ATTRIBUTES_LIST].value, customer_id, bank_id)
	except Exception as e:
		logger.exception(f'Could not get customer_id or create customer attributes: {e}')
	update_customer_body = obp.PutUpdateCustomerNumberJsonV310(
		customer_number=customer_nr
	)
	res2 = customers.update_customer_number(
		body=update_customer_body,
		customer_id=res.customer_id,
		bank_id=bank_id
	)
	return res, res2
