import requests
#my_info if another file contain user access token
from my_info import app_access_token
from termcolor import colored

base_url = 'https://api.instagram.com/v1/'
def self_info():
    request_url  = (base_url + 'users/self/?access_token=%s')%(app_access_token)
    request_object = requests.get(request_url)
    my_info = request_object.json()
    print colored('Your info is:','green'), my_info
    print colored("Your Instagram username is:","green")+(" %s"%(my_info['data']['username']))
    print colored("Your Followers:",'green')+(" %s") % (my_info['data']['counts']['followed_by'])
    print colored('People you Follow:' ,'green')+(" %s") % (my_info['data']['counts']['follows'])
    print colored('No. of posts:' ,"green")+(" %s") % (my_info['data']['counts']['media'])

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
        print 'Status code other than 200 was received!'
        exit()

#use user id to fetch user's information
def friend_info():
    user_id = friend_id()#calling friend_id function to access the id of the user
    if user_id:
        request_url = (base_url + 'users/%s/?access_token=%s') % (user_id,app_access_token)
        request_object = requests.get(request_url)
        info = request_object.json()
        print colored('Your friend\'s info is:', 'green'), info
        print colored("Your friend\'s Follower:", 'green') + (" %s") % (info['data']['counts']['followed_by'])
        print colored('People your friend Follows:', 'green') + (" %s") % (info['data']['counts']['follows'])
        print colored('No. of posts:', "green") + (" %s") % (info['data']['counts']['media'])
    else:
        print colored("User not found", 'red')

print "Enter your choice from the given option:"
print "press:\n1.to get your instagram details\n2.to get your friend's instsgram details"

choice = int(raw_input())
dic = {1:self_info,
       2:friend_info
       }
dic[choice]()

