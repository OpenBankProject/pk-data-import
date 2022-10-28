import unittest
from transactions import create_transaction_from_row, create_transaction_with_attributes_from_row
from openpyxl import Workbook
wb = Workbook()
ws_transactions = wb.create_sheet(title="Transactions")
#  transaction from account to account
ws_transactions['C2'] = "Fred Kubel"  # debtor_legal_name
ws_transactions['D2'] = 'OBP'  # debtor_bank_routing_scheme
ws_transactions['E2'] = 'my_bank2'  # debtor_bank_routing_address
ws_transactions['F2'] = 'Account_Number'  # debtor_account_routing_scheme
ws_transactions['G2'] = '12346678893333383'  # debtor_account_routing_address
ws_transactions['H2'] = "Hans Barff"  # creditor_legal_name
ws_transactions['I2'] = "OBP"  # creditor_bank_routing_scheme
ws_transactions['J2'] = "my_bank2"  # creditor_bank_routing_address
ws_transactions['K2'] = 'Account_Number'  # creditor_account_routing_scheme
ws_transactions['L2'] = '12346678896666673'  # creditor_account_routing_address
ws_transactions['M2'] = '40'  # amount
ws_transactions['N2'] = 'EUR'  # currency
ws_transactions['O2'] = 'my description'  # description
ws_transactions['P2'] = '2022-09-19T02:31:05Z'  # booked_date
ws_transactions['Q2'] = '2022-09-19T06:31:05Z'  # value_date

# transaction from account to counterparty
ws_transactions['C3'] = "Fred Kubel"  # debtor_legal_name
ws_transactions['D3'] = 'OBP'  # debtor_bank_routing_scheme
ws_transactions['E3'] = 'my_bank2'  # debtor_bank_routing_address
ws_transactions['F3'] = 'Account_Number'  # debtor_account_routing_scheme
ws_transactions['G3'] = '12346678893333383'  # debtor_account_routing_address
ws_transactions['H3'] = "Karl Orff"  # creditor_legal_name
ws_transactions['I3'] = "OBP"  # creditor_bank_routing_scheme
ws_transactions['J3'] = "some bank"  # creditor_bank_routing_address
ws_transactions['K3'] = 'Account_Number'  # creditor_account_routing_scheme
ws_transactions['L3'] = '787878787787'  # creditor_account_routing_address
ws_transactions['M3'] = '40'  # amount
ws_transactions['N3'] = 'EUR'  # currency
ws_transactions['O3'] = 'my description'  # description
ws_transactions['P3'] = '2022-09-19T02:31:05Z'  # booked_date
ws_transactions['Q3'] = '2022-09-19T06:31:05Z'  # value_date

# transaction from counterparty to account
ws_transactions['C4'] = "Hugo Schumacher"  # debtor_legal_name
ws_transactions['D4'] = 'OBP'  # debtor_bank_routing_scheme
ws_transactions['E4'] = 'fast bank'  # debtor_bank_routing_address
ws_transactions['F4'] = 'Account_Number'  # debtor_account_routing_scheme
ws_transactions['G4'] = '32342323232'  # debtor_account_routing_address
ws_transactions['H4'] = "Hans Barff"  # creditor_legal_name
ws_transactions['I4'] = "OBP"  # creditor_bank_routing_scheme
ws_transactions['J4'] = "my_bank2"  # creditor_bank_routing_address
ws_transactions['K4'] = 'Account_Number'  # creditor_account_routing_scheme
ws_transactions['L4'] = '12346678896666673'  # creditor_account_routing_address
ws_transactions['M4'] = '40'  # amount
ws_transactions['N4'] = 'EUR'  # currency
ws_transactions['O4'] = 'my description'  # description
ws_transactions['P4'] = '2022-09-19T02:31:05Z'  # booked_date
ws_transactions['Q4'] = '2022-09-19T06:31:05Z'  # value_date
ws_transactions['R4'] = '{ "some_category":  "C", "another_thing": "something"}'


class TestIntegrationTransactionCreation(unittest.TestCase):

	def test_create_transaction_from_to_account(self):
		res = create_transaction_from_row(ws_transactions[2])
		print(res)
		self.assertIsNotNone(res._from.account_id)
		self.assertEqual(res._from.bank_id, 'my_bank2')
		self.assertEqual(res.to.bank_id, 'my_bank2')
		self.assertIsNotNone(res.to.account_id)
		self.assertEqual(res.value.amount, '40')
		self.assertEqual(res.value.currency, 'EUR')

	def test_create_transaction_from_account_to_counterparty(self):
		res = create_transaction_from_row(ws_transactions[3])
		self.assertIsNotNone(res._from.account_id)
		self.assertEqual(res._from.bank_id, 'my_bank2')
		self.assertIsNotNone(res.to.counterparty_id)
		self.assertEqual(res.value.amount, '40')
		self.assertEqual(res.value.currency, 'EUR')

	def test_create_transaction_from_counterparty_to_account(self):
		res = create_transaction_from_row(ws_transactions[4])
		self.assertIsNotNone(res._from.counterparty_id)
		self.assertEqual(res.to.bank_id, 'my_bank2')
		self.assertIsNotNone(res.to.account_id)
		self.assertEqual(res.value.amount, '40')
		self.assertEqual(res.value.currency, 'EUR')
		print(res)


if __name__ == '__main__':
	unittest.main()