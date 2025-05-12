import base64
import hashlib
import hmac
import json
import time


def base64url_encode(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b'=').decode()


def base64url_decode(data: str) -> bytes:
    padding = '=' * (-len(data) % 4)  # 补足 base64 padding
    return base64.urlsafe_b64decode(data + padding)


def jwt_encode(payload: dict, secret: str) -> str:
    header = {'alg': 'HS256', 'typ': 'JWT'}
    header_b64 = base64url_encode(json.dumps(header, separators=(',', ':')).encode())
    payload_b64 = base64url_encode(json.dumps(payload, separators=(',', ':')).encode())
    signing_input = f"{header_b64}.{payload_b64}".encode()
    signature = hmac.new(secret.encode(), signing_input, hashlib.sha256).digest()
    signature_b64 = base64url_encode(signature)
    return f"{header_b64}.{payload_b64}.{signature_b64}"


def jwt_decode(token: str, secret: str) -> dict:
    header_b64, payload_b64, signature_b64 = token.split('.')
    signing_input = f"{header_b64}.{payload_b64}".encode()
    expected_sig = hmac.new(secret.encode(), signing_input, hashlib.sha256).digest()
    expected_sig_b64 = base64url_encode(expected_sig)
    if not hmac.compare_digest(expected_sig_b64, signature_b64):
        raise ValueError("Invalid signature")
    payload = json.loads(base64url_decode(payload_b64))
    # 可选: 检查过期时间
    if 'exp' in payload and time.time() > payload['exp']:
        raise ValueError("Token expired")
    return payload



d = {
  "sub": "1234567890",
  "name": "Ginger Garren",
  "iat": 1516239022
}

jwt_encode(d, 'super secret key!!!')
# https://jwt.io/
