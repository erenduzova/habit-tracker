# habit-tracker-water
Habit tracker app for drinking water.

## Table of Contents
* [General Info](#general-info)
* [Built With](#built-with)
* [Environment Variables](#environment-variables)
* [Requests](#requests)
* [Accessing Graphs](#accessing-graphs)

## General Info
This project is a simple tracker app for tracking how much water user drinks a day and saves it using pixela .

## Built With
Project is created with:
* Python version: 3.10
* python-dotenv version: 0.21.0
* requests version: 2.28.1
* pixela

## Environment Variables
I used ".env" file to store environment variables for security reasons.<br />
In this file I stored username and pixela token.<br />
You should create this file with your information or write yours to the main.py and do not use ".env" file.<br />
```
PIXELA_TOKEN=**********    Validation rule: [ -~]{8,128}
USER_NAME=*****    Validation rule: [a-z][a-z0-9-]{1,32}
```

## Requests
All requests commented out.<br />
Because we only need to create user once, post same graph once ...<br />
Uncomment which request you want to use, run the code and comment out requests again.<br />
```
# # Post User
# response_user = requests.post(url=pixela_endpoint, json=USER_PARAMS)
# print(response_user.text)

# # Post Graph
# response_gr = requests.post(url=graphs_endpoint, json=GRAPH_PARAMS, headers=headers)
# print(response_gr.text)

# # Post Pixel
# response_px = requests.post(url=post_pixel_endpoint, json=POST_PIXEL_PARAMS, headers=headers)
# print(response_px.text)

# # Update Pixel
# response_up_px = requests.put(url=put_pixel_endpoint, json=PUT_PIXEL_PARAMS, headers=headers)
# print(response_up_px.text)

# # Delete Pixel
# response_del_px = requests.delete(url=del_pixel_endpoint, headers=headers)
# print(response_del_px.text)
```

## Accessing Graphs
Go to this url: "https://pixe.la/v1/users/{username}/graphs/{graph-id}.html" <br />
Change username and graph-id with yours.
