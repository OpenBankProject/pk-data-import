from obp_client import client, logger
import obp_python as obp
from obp_python.rest import ApiException

products = obp.ProductApi(client)


def create_product_if_not_exist(product_code, bank_id):

	try:
		products.get_product(product_code, bank_id)
		logger.debug(f'Product {product_code} already exists')
	except ApiException:
		logger.debug(f'Creating Product {product_code}')
		body = obp.PutProductJsonV500(
			name=product_code,
			parent_product_code=''
		)
		products.create_product(body=body, product_code=product_code, bank_id=bank_id)
