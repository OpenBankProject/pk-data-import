import obp_python as obp
from obp_client import client, token, obp_host, logger
import requests

bank_id = "my_bank2"
account_id = 'a8b40caf-a510-4e49-a5d6-37be53cbae98'
customer_account_link = {
	"customer_id":"7uy8a7e4-6d02-40e3-a129-0b2bf89de8uh",
	"account_id":"8ca8a7e4-6d02-40e3-a129-0b2bf89de9f0",
	"relationship_type":"sole owner" # alternative: joint owner
}
customer_owner = "621609002"

customer_owners = '1234063, 1234363, 123456'
accounts_api = obp.AccountApi(client)
customer_api = obp.CustomerApi(client)


def create_customer_account_link(bank_id, customer_id, account_id, relationship_type):
	headers = {
		'Content-Type': 'application/json',
		'Authorization': f'DirectLogin token={token}'
	}

	payload = {
		"customer_id": customer_id,
		"account_id": account_id,
		"relationship_type": relationship_type
	}

	url = f'{obp_host}/obp/v5.0.0/banks/{bank_id}/customer-account-links'
	req = requests.post(url, headers=headers, json=payload)
	return req


def get_customer_account_links_for_customer(bank_id, customer_id):
	headers = {
		'Content-Type': 'application/json',
		'Authorization': f'DirectLogin token={token}'
	}

	url = f'{obp_host}/obp/v5.0.0/banks/{bank_id}/customers/{customer_id}/customer-account-links'
	req = requests.get(url, headers=headers)
	return req


def get_customer_account_links_for_account(bank_id, account_id):
	headers = {
		'Content-Type': 'application/json',
		'Authorization': f'DirectLogin token={token}'
	}

	url = f'{obp_host}/obp/v5.0.0/banks/{bank_id}/accounts/{account_id}/customer-account-links'
	req = requests.get(url, headers=headers)
	return req


def get_customer_list_from_value(value):
	return [x.strip() for x in value.split(',')]


def get_customer_ids_from_customer_numbers(customer_nrs, bank_id):
	customer_ids = []
	for customer_nr in customer_nrs:
		body = obp.PutUpdateCustomerNumberJsonV310(
			customer_number=customer_nr
		)
		customer = customer_api.get_customer_by_customer_number(
			body=body, bank_id=bank_id
		)
		customer_ids.append(customer.customer_id)
	return customer_ids


def create_joint_customer_account_links(joint_customer_nrs, bank_id, account_id):
	customer_list = get_customer_list_from_value(joint_customer_nrs)
	customer_ids = get_customer_ids_from_customer_numbers(customer_list, bank_id)
	for customer_id in customer_ids:
		try:
			res = create_customer_account_link(
				bank_id=bank_id,
				customer_id=customer_id,
				account_id=account_id,
				relationship_type='joint owner'
			)
			logger.debug(res.text)
		except Exception as e:
			logger.exception(f'Could not create customer account link for customer {customer_id}, account {account_id}: {e}')


def create_sole_customer_account_link(customer_nr, bank_id, account_id,):
	clean_customer_nr = str(customer_nr).strip()
	body = obp.PutUpdateCustomerNumberJsonV310(
		customer_number=clean_customer_nr
	)
	customer = customer_api.get_customer_by_customer_number(
		body=body, bank_id=bank_id
	)
	logger.debug(f'Get Customernr {clean_customer_nr}:\n {customer}')
	res = create_customer_account_link(
		bank_id=bank_id,
		customer_id=customer.customer_id,
		account_id=account_id,
		relationship_type='sole owner'
	)
	logger.debug(f' trying to create customer account link: {res.text}')

