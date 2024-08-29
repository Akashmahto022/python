import requests

# URL of the API endpoint
url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"

# Making the GET request
response = requests.get(url)

# Checking if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    print(data)
else:
    print(f"Failed to retrieve data: {response.status_code}")
