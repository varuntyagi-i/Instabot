import urllib
import requests
#my_info contains file contain user access token
from my_info import app_access_token,base_url
from termcolor import colored
from UserId import friend_id

def get_own_post():
    request_url = (base_url + 'users/self/media/recent/?access_token=%s') % (app_access_token)
    print '\nGET request url : %s' % (request_url)
    own_media = requests.get(request_url).json()
    if own_media['meta']['code'] == 200:
        if len(own_media['data']):
            #return own_media['data'][0]['id']
            image_name = own_media['data'][0]['id'] + '.jpeg'
            image_url = own_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print colored('Your recent post has been downloaded!','green')
        else:
            print 'Post does not exist!'
            exit()
    else:
        # if access token is wrong an error message gets printed
        print colored(own_media['meta']['error_message'], 'red')
        exit()


def get_user_post():
    user_id = friend_id()
    if user_id:
        request_url = (base_url + 'users/%s/media/recent/?access_token=%s') % (user_id, app_access_token)
        print '\nGET request url : %s' % (request_url)
        user_media = requests.get(request_url).json()
        if user_media['meta']['code'] == 200:
            if len(user_media['data']):
                #return user_media['data'][0]['id']
                image_name = user_media['data'][0]['id'] + '.jpeg'
                image_url = user_media['data'][0]['images']['standard_resolution']['url']
                urllib.urlretrieve(image_url, image_name)
                print colored('Your friend\'s recent post has been downloaded!','green')
            else:
                print "There is no recent post!"
                exit()
        else:
            print colored(user_media['meta']['error_message'], 'red')
            exit()
    else:
        # if user enter wrong user name which does not exist
        print colored("User not found", 'red')
        exit()
