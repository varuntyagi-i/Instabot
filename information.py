import requests
from UserId import friend_id
from termcolor import colored
#my_info contains file contain user access token
from my_info import base_url,app_access_token

def self_info():
    request_url  = (base_url + 'users/self/?access_token=%s')%(app_access_token)
    request_object = requests.get(request_url)
    my_info = request_object.json()
    if my_info['meta']['code'] == 200:
        print colored('Your info is:', 'green'), my_info
        print colored("Your Instagram username is:", "green") + (" %s" % (my_info['data']['username']))
        print colored("Your Followers:", 'green') + (" %s") % (my_info['data']['counts']['followed_by'])
        print colored('People you Follow:', 'green') + (" %s") % (my_info['data']['counts']['follows'])
        print colored('No. of posts:', "green") + (" %s") % (my_info['data']['counts']['media'])
    else:
#if access token is wrong an error message gets printed
        print colored(my_info['meta']['error_message'],'red')



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
#if user enter wrong user name which does not exist
        print colored("User not found", 'red')
