import requests
from my_info import base_url,app_access_token
from termcolor import colored

def get_media_id(user_id):
    request_url = (base_url + "users/" + user_id + "/media/recent/?access_token=%s") % (app_access_token)
    request_object = requests.get(request_url)
    info = request_object.json()
    # fetching user's id
    if info['meta']['code'] == 200:
        if len(info["data"]):
            print colored("Select a post from the given post below","yellow")
            count = 0
            #displaying url of every post user posted till now.
            for ele in info["data"]:
                count += 1
                print "%d. post's url: %s"%(count,ele["images"]["standard_resolution"]["url"])
            print colored("Enter url no: ","yellow")
            #to check whether user selects right option or not
            while True:
                value = int(raw_input())-1
                if 0 <= value <= count-1:
                    break
                else:
                    print colored("Wrong selection,re-enter your choice",'red')
                    pass
            return info["data"][value]["id"]
        else:
            return False
    else:
        # if access token is wrong an error message gets printed
        print info['meta']['error_message']
        exit()

