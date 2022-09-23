from dotenv import load_dotenv
import os
import requests
from datetime import date, datetime

load_dotenv()

USERNAME = os.getenv("USER_NAME")
TOKEN = os.getenv("PIXELA_TOKEN")

# Date
TODAY = date.today()

# Change year, month, day to date you want to update
UPDATE_DAY = datetime(year=2022, month=9, day=23).strftime("%Y%m%d")

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

# Put Pixel Parameters
PUT_PIXEL_PARAMS = {
    "quantity": "1.8" # Add 1 glass more and update
}

# Endpoints
pixela_endpoint = "https://pixe.la/v1/users"
graphs_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs"
post_pixel_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_PARAMS['id']}"
put_pixel_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_PARAMS['id']}/{UPDATE_DAY}"

# # Post User
# response_user = requests.post(url=pixela_endpoint, json=USER_PARAMS)
# print(response_user.text)
#
# # Post Graph
# response_gr = requests.post(url=graphs_endpoint, json=GRAPH_PARAMS, headers=headers)
# print(response_gr.text)
#
# # Post Pixel
# response_px = requests.post(url=post_pixel_endpoint, json=POST_PIXEL_PARAMS, headers=headers)
# print(response_px.text)

# Update Pixel
response_up_px = requests.put(url=put_pixel_endpoint, json=PUT_PIXEL_PARAMS, headers=headers)
print(response_up_px.text)