from urllib.parse import urlencode
import json


file_path = 'client_secret.json'

# Open the file and load its contents
with open(file_path, "r") as json_file:
    data = json.load(json_file)
    print('data', data)
    client_id = data['web']['client_id']
    client_secret = data['web']['client_secret']

# redirect_uri = GOOGLE_REDIRECT_URI
redirect_uri = 'https://www.baidu.com'
scope = 'https://www.googleapis.com/auth/userinfo.email'

# state: 自定义的字段， 生成 authorization url 的时候确定
#  后续拿到 auth code 的时候这个 state 也会返回
state = 'wozhaoritianzuiniubi'

raw_get_params = {
    'response_type': 'code',
    'client_id': client_id,
    'redirect_uri': redirect_uri,
    'scope': scope,
    'state': state,
    'access_type': 'offline',
    'include_granted_scopes': 'true',
    # 'login_hint': 'hint@example.com',
    'prompt': 'consent',
}

encoded_params = urlencode(raw_get_params)
authorization_url = 'https://accounts.google.com/o/oauth2/auth?' + encoded_params

authorization_url

