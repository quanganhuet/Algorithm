import jwt
import base64
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa

def jwk_to_rsa_public_key(jwk):
    key_modulus = base64.urlsafe_b64decode(jwk["n"] + '==')
    key_exponent = base64.urlsafe_b64decode(jwk["e"] + '==')
    
    public_key_numbers = rsa.RSAPublicNumbers(
        int.from_bytes(key_exponent, 'big'),
        int.from_bytes(key_modulus, 'big')
    )
    
    return public_key_numbers.public_key(default_backend())

# Example JWK
jwk_example = {
    "kty": "RSA",
    "e": "AQAB",
    "use": "sig",
    "kid": "example-key", 
    "alg": "RS256",
    "n": "yRfFBkzlaZK496G6DG5U7yZaqzPa4cZ0XEYm7fLqYDDbPFrjAsBED-FuBEo-0lDZa1mo9EW-hnSXJBjjwWKxVoYGxRtgJz8yBRuhSKt3O8y4FYykCypYpdrL5F4OZJH_vl435iKRwhoYw33sBTtva1-9LEc96oUCPaJ3jbJ0VIMbPJihc1yvHum3n-cohMxS-jwTILrtusAwIRWG2s4csVnnDszkKYu-YKzEesgoTEBeksvXT6r_Gs4b3MkgDBLal85MB0OACD1oCOO1z9uwfenKDJjgUCo34_8V17KHqKU2yfTi4VQQNlg_YoEYIHlO4DlPHKzLZw-DOt1Owxdv-Q"
}

# Convert JWK to RSA public key
public_key = jwk_to_rsa_public_key(jwk_example)

# Your JWT token
jwt_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbmxvY2FsIiwiYXVkIjpbIm9hdXRoMi1yZXNvdXJjZSJdLCJ1c2VyX25hbWUiOiJhZG1pbmxvY2FsIiwic2NvcGUiOlsicmVhZCJdLCJleHAiOjE3MDA3MTQ3MzcsImlhdCI6MTcwMDcxMTEzNywianRpIjoiNjQ4ZGNkMDgtNzJkMS00NDZhLTg3ZTctZDMwYzZkMzA4NzAxIiwiY2xpZW50X2lkIjoiZGVhZGJlZWYtZGVhZC1iZWVmLWRlYWQtYmVlZmRlYWRiZWVmIn0.PbqPORd73WZcosnHSa2C67Wh-3bF8sd2rn9vq5ltPdOSwHm1r12Kv2P7f1GSV6lWdSgZ_hjKohMAOaPEdYAPTcDXiW0IVZ-_ulGOmtVbnItrUk5jQPy-bsFwceQigMxAPAN9uY7PcqbheFzVgh1jG6vo_1VgardzuPU1dmB84bHH9nCwbxZ3anX9mw1ETyaQge7hEKqA52KtSTcifZgGlH_Dgf9092_bAYrcvFyac3sIZaQfzDYRb5yrIfffPRn5TJbTJEDIqU55f95Eij_lVvJfcbD_VVnVgE5PXiqBsh_RPm92oPTri4msouFQChL35kfWk078ieF3kFdWYMY6Rw"

# Verify the JWT signature using the public key
try:
    decoded_token = jwt.decode(jwt_token, public_key, algorithms=["RS256"])
    print("JWT is valid:", decoded_token)
except jwt.ExpiredSignatureError:
    print("JWT has expired.")
except jwt.InvalidTokenError:
    print("Invalid JWT signature.")
