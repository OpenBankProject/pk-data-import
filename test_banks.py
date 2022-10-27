import unittest
from banks import create_bank_request_body_from_row, create_bank_from_row
from  openpyxl import Workbook
from obp_python import BankRoutingJsonV121
wb = Workbook()
ws_banks = wb.create_sheet(title="Banks")
ws_banks['A2'] = "my_bank2"
ws_banks['B2'] = "My Bank"
ws_banks['C2'] = "My Bank Limited"
ws_banks['D2'] = 'http://mylogo'
ws_banks['E2'] = 'http://mywebsite'
ws_banks['F2'] = 'OBP'
ws_banks['G2'] = 'my_bank2'
ws_banks['H2'] = None


class TestBankCreation(unittest.TestCase):

	def test_create_bank_request_body(self):
		bank_request_body = create_bank_request_body_from_row(ws_banks[2])
		self.assertEqual(bank_request_body.id, 'my_bank2')
		self.assertEqual(bank_request_body.bank_code, "My Bank")
		self.assertEqual(bank_request_body.full_name, "My Bank Limited")
		self.assertEqual(bank_request_body.logo, 'http://mylogo')
		self.assertEqual(bank_request_body.website, 'http://mywebsite')
		self.assertEqual(bank_request_body.bank_routings, [BankRoutingJsonV121(
			scheme='OBP', address='my_bank2'
		)])


if __name__ == '__main__':
	unittest.main()
