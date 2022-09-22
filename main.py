from dotenv import load_dotenv
import os
import requests

load_dotenv()

USERNAME = os.getenv("USER_NAME")
TOKEN = os.getenv("PIXELA_TOKEN")

# User Parameters
USER_PARAMS = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Endpoints
pixela_endpoint = "https://pixe.la/v1/users"

# Post User
response = requests.post(url=pixela_endpoint, json=USER_PARAMS)
print(response.text)
