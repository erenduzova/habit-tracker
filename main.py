from dotenv import load_dotenv
import os
import requests

load_dotenv()

USERNAME = os.getenv("USER_NAME")
TOKEN = os.getenv("PIXELA_TOKEN")

headers = {
    "X-USER-TOKEN": TOKEN
}

# User Parameters
USER_PARAMS = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Graph Parameters
GRAPH_PARAMS = {
    "id": "graph-water1",
    "name": "Drinking Water Graph",
    "unit": "L",
    "type": "float",
    "color": "sora"
}

# Endpoints
pixela_endpoint = "https://pixe.la/v1/users"
graphs_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs"

# Post User
response_user = requests.post(url=pixela_endpoint, json=USER_PARAMS)
print(response_user.text)

# Post Graph
response_gr = requests.post(url=graphs_endpoint, json=GRAPH_PARAMS, headers=headers)
print(response_gr.text)
