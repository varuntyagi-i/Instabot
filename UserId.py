import requests
#my_info contains file contain user access token
from my_info import base_url,app_access_token

def friend_id():
    user_name = raw_input("Enter friend's name:")
#Endpoint to access user's id
    request_url = (base_url + "users/search?q=%s&access_token=%s")%(user_name,app_access_token)
    request_object = requests.get(request_url)
    info = request_object.json()
#fetching user's id
    if info['meta']['code'] == 200:
        if len(info["data"]):
            return info["data"][0]["id"]
        else:
            return False
    else:
# if access token is wrong an error message gets printed
        print info['meta']['error_message']
        exit()

