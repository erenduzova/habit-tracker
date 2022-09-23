from dotenv import load_dotenv
import os
import requests
from datetime import date

load_dotenv()

USERNAME = os.getenv("USER_NAME")
TOKEN = os.getenv("PIXELA_TOKEN")

# Date
TODAY = date.today()

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
    "color": "sora",
    "timezone": "Turkey"
}

# Pixel Post Parameters
POST_PIXEL_PARAMS = {
    "date": TODAY.strftime("%Y%m%d"),
    "quantity": "1.6"  # 8 glass of water
}

# Endpoints
pixela_endpoint = "https://pixe.la/v1/users"
graphs_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs"
post_pixel_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_PARAMS['id']}"

# # Post User
# response_user = requests.post(url=pixela_endpoint, json=USER_PARAMS)
# print(response_user.text)
#
# # Post Graph
# response_gr = requests.post(url=graphs_endpoint, json=GRAPH_PARAMS, headers=headers)
# print(response_gr.text)
#
# Post Pixel
response_px = requests.post(url=post_pixel_endpoint, json=POST_PIXEL_PARAMS, headers=headers)
print(response_px.text)
