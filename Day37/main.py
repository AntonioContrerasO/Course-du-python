import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "lilbean"
TOKEN = "Antonelo12"
GRAPH_ID = "graph1"


user_params  = {
    "token":"Antonelo12",
    "username":"lilbean",
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)
graph_endpoint_create = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
# graphs_config = {
#     "id":"graph1",
#     "name":"100 Days of code",
#     "unit":"Days",
#     "type":"int",
#     "color":"momiji"
# }
today = datetime(year=2022,month=1,day=9)
formatted_today = today.strftime("%Y%m%d")
graph_endpoint_update_delete = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{formatted_today}"
# pixel_create = {
#     "":
#
# }

pixel_update = {
    "quantity":"35"
}

headers = {
    "X-USER-TOKEN":TOKEN
}

response = requests.delete(url=graph_endpoint_update_delete, headers=headers)
print(response.text)