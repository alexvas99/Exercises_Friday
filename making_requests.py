import requests
from pprint import pprint

POSTCODE_ENDPOINT = "https://api.postcodes.io/postcodes/"

# response = requests.get(POSTCODE_ENDPOINT + "EC2Y 5AS")

# print(f"\nStatus code: {response.status_code}\n")
# print(f"Headers: {response.headers}\n")
# print(f"Content: {response.content}\n")
# print(f"Content Type: {response.content}\n")

# print(f"JSON: {response.json}")

# if response.status_code == 200:
#     response_json = response.json()
#     print(response_json.keys())
#     result = response_json["result"]
#     pprint(result)

# Create a function `postcode_lookup` that takes in a postcode
# and calls the postcodes api
# and prints the latitude and longitude of that location
# in a readable way

# def postcode_lookup(postcode):
#     response = requests.get(POSTCODE_ENDPOINT + postcode)

#     if response.status_code == 200:
#         response_json = response.json()

#         latitude = response_json["result"]["latitude"]
#         longitude = response_json["result"]["longitude"]

#         print("Latitude:", latitude)
#         print("Longitude:", longitude)
#     else:
#         print("Postcode not found")

# postcode = input("Enter postcode: ")
# postcode_lookup(postcode)

headers = {"Content-Type": "application/json"}

body = {
    "postcodes": ["PR3 0SG", "M45 6GN", "EX165BL"]
}

response = requests.post(
    url=POSTCODE_ENDPOINT,
    headers=headers,
    json=body
)

list_of_results = response.json().get("result")
pprint(list_of_results, sort_dicts=False)

for single_postcode_data in list_of_results:
    print(type(single_postcode_data), single_postcode_data)
    result = single_postcode_data["result"]
    print(f"{result[postcode]} - Eastings {result["eastings"]}, Northings: {result["northings"]}")





    # if item["result"] is not None:
    #     postcode = item["result"]["postcode"]
    #     eastings = item["result"]["eastings"]
    #     northings = item["result"]["northings"]

    #     print(f"{postcode}: Eastings = {eastings}, Northings = {northings}")
    # else:
    #     print(f"{query_postcode}: postcode not found")