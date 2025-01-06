import json

import requests
# from account.third_party_login.google_login_utils import *

# file_path = GOOGLE_CLIENT_SECRET_FILE
file_path = 'client_secret.json'
redirect_uri = 'https://www.baidu.com'

# Open the file and load its contents
with open(file_path, "r") as json_file:
    data = json.load(json_file)
    print('data', data)
    client_id = data['web']['client_id']
    client_secret = data['web']['client_secret']
# 用 auth code 来换 access_token 的 URL
url = "https://oauth2.googleapis.com/token"

# 这里的 code 就是 auth_code
code = '4/0AanRRrtXNkhBqeCDVRio_RJsz1jzkCsMQUrXhwrkkZ_stny8G_oOIBkSNMNOgJJjzo36dw'

data = {
    "code": code,
    "client_id": client_id,
    "client_secret": client_secret,
    "redirect_uri": redirect_uri,
    "grant_type": "authorization_code",
}

# 发送 POST 请求
resp = requests.post(url, data=data)

resp.json()
access_token = resp.json()['access_token']
headers = {
    'Authorization': 'Bearer ' + access_token,
}
resp = requests.get(headers=headers, url='https://www.googleapis.com/oauth2/v3/userinfo')
resp.json()
resp.json()['email']
