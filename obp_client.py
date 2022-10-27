import obp_python as obp
import os
from dotenv import load_dotenv
from get_direct_login_token import createDirectLoginToken
import logging


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("obp")
logger.propagate = True
load_dotenv()

obp_host = os.getenv('OBP_HOSTNAME')
configuration = obp.Configuration()
configuration.client_side_validation = False
configuration.host = os.getenv('OBP_HOSTNAME')
username = os.getenv('OBP_USERNAME')
password = os.getenv('OBP_PASSWORD')
consumer_key = os.getenv('OBP_CONSUMER_KEY')
token = createDirectLoginToken(username, password, consumer_key, configuration.host)
configuration.api_key['Authorization'] = f'DirectLogin token={token}'
client = obp.ApiClient(configuration)
api_instance = obp.APIApi(client)
user_instance = obp.UserApi(client)
empty_body = '{}' # EmptyClassJson | EmptyClassJson object that needs to be added.
api_version = 'v5.0.0' # str | eg:v2.2.0, v3.0.0


