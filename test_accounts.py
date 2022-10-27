import unittest
import obp_python as obp
from accounts import get_create_account_request_body_from_row
from  openpyxl import Workbook
wb = Workbook()
ws_accounts = wb.create_sheet(title="Customers")
ws_accounts['A2'] = "my_bank2"
ws_accounts['B2'] = "my_product"
ws_accounts['C2'] = "1234063"
ws_accounts['D2'] = '1234063, 1234363, 123456'
ws_accounts['I2'] = 'EUR'
ws_accounts['M2'] = 'Account_Number'
ws_accounts['N2'] = '12398766'
ws_accounts['P2'] = None


class TestAccountsCreation(unittest.TestCase):

	def test_create_account_request_body(self):
		body = get_create_account_request_body_from_row(ws_accounts[2])
		print(body)
		self.assertEqual(body.product_code, "my_product")
		self.assertEqual(body.balance, obp.AmountOfMoneyJsonV121(currency='EUR', amount='0'))
		self.assertEqual(body.account_routings, [obp.AccountRoutingJsonV121(scheme='Account_Number', address='12398766')])


if __name__ == '__main__':
	unittest.main()