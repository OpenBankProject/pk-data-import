from accounts import create_account_with_customer_links_from_row
from openpyxl import Workbook
wb = Workbook()
ws_accounts = wb.create_sheet(title="Accounts")
ws_accounts['A2'] = "my_bank2"
ws_accounts['B2'] = "my_product"
ws_accounts['D2'] = '1234363, 123456'
ws_accounts['I2'] = 'EUR'
ws_accounts['M2'] = 'Account_Number'
ws_accounts['N2'] = '12346678896666673'
ws_accounts['P2'] = None
ws_accounts['A3'] = "my_bank2"
ws_accounts['B3'] = "my_product"
ws_accounts['C3'] = "621609002"
ws_accounts['I3'] = 'EUR'
ws_accounts['M3'] = 'Account_Number'
ws_accounts['N3'] = '12346678893333383'
ws_accounts['P3'] = None

res = create_account_with_customer_links_from_row(ws_accounts[2])
print(res)
res = create_account_with_customer_links_from_row(ws_accounts[3])
print(res)
