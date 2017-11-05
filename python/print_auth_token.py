import fb_auth_token
import sys

email = sys.argv[1]
password = sys.argv[2]

token = fb_auth_token.get_fb_access_token(email, password)
fb_id = fb_auth_token.get_fb_id(token)

print token
print fb_id
