import requests
from json import loads


def createDirectLoginToken(username, user_password, consumer_key, obp_api_host, verify=True):
	authorization = f"DirectLogin username={username},password={user_password},consumer_key={consumer_key}"
	headers = {'Content-Type': 'application/json', 'Authorization': authorization}

	payload = None
	url = obp_api_host + "/my/logins/direct"
	try:
		req = requests.post(url, headers=headers, json=payload, verify=verify)
		token = loads(req.text)["token"]
	except Exception as e:
		# no logger here to not have circle dependencies with obp_client
		print(f'could not get direct login for: {url} user: {username}: {e}')
		token = None
	return token
