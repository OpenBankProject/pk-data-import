import obp_python as obp
from obp_python.rest import ApiException
from obp_client import client, logger
from banks import get_bank_id_from_str
from products import create_product_if_not_exist
from customer_account_links import create_sole_customer_account_link, create_joint_customer_account_links
from json import loads
import constants as c


accounts = obp.AccountApi(client)
products = obp.ProductApi(client)


def create_account_attributes(attributes_list, product_code, account_id, bank_id):
	try:
		logger.debug(f'attributes_list: {attributes_list}')
		attributes_dict = loads(attributes_list)
		for k, v in attributes_dict.items():
			logger.debug(f'creating account attribute {k}: {v}')
			body = obp.AccountAttributeJson(
				name=k,
				type='STRING',
				value=v
			)
			accounts.create_account_attribute(
				body=body,
				product_code=product_code,
				account_id=account_id,
				bank_id=bank_id
			)
	except Exception as e:
		logger.exception(f'could not create account attributes: {e}')


def get_create_account_request_body_from_row(row):
	product_code = row[c.PRODUCT_CODE].value
	bank_id = get_bank_id_from_str(row[c.BANK_ID].value)
	create_product_if_not_exist(product_code=product_code, bank_id=bank_id)
	account_routing = obp.models.AccountRoutingJsonV121(
		scheme=str(row[c.ACCOUNT_ROUTING_SCHEME].value).strip(),
		address=str(row[c.ACCOUNT_ROUTING_ADDRESS].value).strip()

	)

	account_balance = obp.models.AmountOfMoneyJsonV121(
		currency=row[c.ACCOUNTS_CURRENCY].value.strip(),
		amount="0"
	)
	if row[c.LABEL].value:
		label = row[c.LABEL].value
	else:
		label = ""
	if row[c.BRANCH_ROUTING_ADDRESS].value:
		branch_id = row[c.BRANCH_ROUTING_ADDRESS].value
	else:
		branch_id = ''
	body = obp.CreateAccountRequestJsonV500(
		user_id='',
		branch_id=branch_id,
		account_routings=[account_routing],
		label=label,
		balance=account_balance,
		product_code=product_code
	)
	return body



def create_account_from_row(row):
	res = accounts.add_account(
		bank_id=get_bank_id_from_str(row[c.BANK_ID].value),
		body=get_create_account_request_body_from_row(row))
	return res


def create_account_with_customer_links_from_row(row):
	bank_id = get_bank_id_from_str(row[c.BANK_ID].value)
	product_code = row[c.PRODUCT_CODE].value
	account_id = create_account_from_row(row).account_id

	create_account_attributes(
		attributes_list=row[c.ACCOUNT_ATTRIBUTES_LIST].value,
		account_id=account_id,
		product_code=product_code,
		bank_id=bank_id
	)
	if row[c.CUSTOMER_OWNER_IDS].value is None and row[c.OWNERSHIP_TYPE].value:
		create_joint_customer_account_links(
			joint_customer_nrs=row[c.OWNERSHIP_TYPE].value,
			bank_id=bank_id,
			account_id=account_id
		)
	if row[c.CUSTOMER_OWNER_IDS].value and row[c.OWNERSHIP_TYPE].value is None:
		create_sole_customer_account_link(
			customer_nr=row[c.CUSTOMER_OWNER_IDS].value,
			account_id=account_id,
			bank_id=bank_id
		)


def check_account_exists(bank_id, routing_scheme, routing_address):
	account_routing = obp.models.AccountRoutingJsonV121(
		scheme=routing_scheme,
		address=routing_address

	)
	body = obp.BankAccountRoutingJson(
		bank_id=bank_id,
		account_routing=account_routing
	)
	try:
		res = accounts.get_account_by_account_routing(body=body)
		return res.id
	except ApiException:
		return False
	except Exception as e:
		logger.exception(f'Get account by account routing breaks: {e}')

