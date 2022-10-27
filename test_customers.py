import unittest
from customers import get_create_customer_request_body_from_row, create_customer_from_row
from  openpyxl import Workbook
wb = Workbook()
ws_customers = wb.create_sheet(title="Customers")
ws_customers['A2'] = "my_bank2"
ws_customers['B2'] = "123456"
ws_customers['C2'] = "Hans Meiser"
ws_customers['D2'] = '0123-45678'
ws_customers['E2'] = 'test@test.com'
ws_customers['I2'] = 'Son-of-Moog'



class TestCustomerCreation(unittest.TestCase):

	def test_create_customer_request_body(self):
		body = get_create_customer_request_body_from_row(ws_customers[2])
		self.assertEqual(body.legal_name, "Hans Meiser")
		self.assertEqual(body.mobile_phone_number, '0123-45678')
		self.assertEqual(body.email, 'test@test.com')
		self.assertEqual(body.name_suffix, 'Son-of-Moog')


if __name__ == '__main__':
	unittest.main()