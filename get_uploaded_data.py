from obp_client import client, empty_body
import obp_python as obp

# CHANGE bank_id here
bank_id = 'Telenor'

customer_api = obp.CustomerApi(client)
customers = customer_api.get_customers_at_one_bank(
	body=empty_body,
	bank_id=bank_id
)
print('Customers:\n\n\n')
print(customers)

account_api = obp.AccountApi(client)
accounts = account_api.get_fast_firehose_accounts_at_one_bank(bank_id=bank_id)
print('Accounts: \n\n\n')
print(accounts)
account_ids = [x.id for x in accounts.accounts]

number_of_transactions = 0
transaction_api = obp.TransactionFirehoseApi(client)
for account_id in account_ids:
	transactions = transaction_api.get_firehose_transactions_for_bank_account(
		body=empty_body,
		view_id='owner',
		bank_id=bank_id,
		account_id=account_id
	)
	print('Transactions:\n\n\n')
	print(transactions)
	number_of_transactions += len(transactions.transactions)

print('SUMMARY: \n\n')
print(f'Customers total: {len(customers.customers)}')
print(f'Accounts total: {len(account_ids)}')
print(f'Transactions total {number_of_transactions}')
