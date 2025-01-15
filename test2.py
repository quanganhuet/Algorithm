import hashlib

# Inputs
username = "admin"
realm = "Login to bdd230052dc19c341fdd7ff54fd0e84b"
password = "admin123"
nonce = "235769355"
cnonce = "0a4f113b"
http_method = "GET"
url = "/cgi-bin/magicBox.cgi?action=getLanguageCaps"
qop = "auth"
nc = "00000001"
opaque="25cf7e5b8c488c106493ae167bbfce43be67f71e"
# Calculate HA1

ha1_raw = f"{username}:{realm}:{password}"
ha1 = hashlib.md5(ha1_raw.encode()).hexdigest()

# Calculate HA2
ha2_raw = f"{http_method}:{url}"
ha2 = hashlib.md5(ha2_raw.encode()).hexdigest()

# Calculate Response
response_raw = f"{ha1}:{nonce}:{nc}:{cnonce}:{qop}:{ha2}"
response = hashlib.md5(response_raw.encode()).hexdigest()
# Print results
print("HA1:", ha1)
print("HA2:", ha2)
print("Response Md5:", response)

print(f'Digest username="admin", realm="{realm}",nc=00000001, cnonce="{cnonce}", qop="auth", opaque="{opaque}", nonce="{nonce}", uri="/cgi-bin/magicBox.cgi?action=getLanguageCaps",response="{response}"')