from transactions import create_transaction_from_row
from openpyxl import Workbook
wb = Workbook()
ws_transactions = wb.create_sheet(title="Transactions")
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


res = create_transaction_from_row(ws_transactions[2])
print(res)

