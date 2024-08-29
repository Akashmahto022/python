import requests

def fetch_random_user():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()
    # print(data)
    
    if data["success"] and "data" in data:
        userData = data["data"] 
        # print(userData)
        userName = userData["login"]["username"]
        location = userData["location"]["country"]
        return userName, location
    else:
        raise Exception("Failed to fetch user data")

def main():
    try:
        userName, location = fetch_random_user()
        print(f"User Name: {userName} \nCountry: {location}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
