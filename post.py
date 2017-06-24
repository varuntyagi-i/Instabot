import urllib
import requests
import numpy as np
#my_info contains file contain user access token
from my_info import app_access_token,base_url
from termcolor import colored
from UserId import friend_id
from MediaId import get_media_id

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

def recent_like():
    request_url = (base_url + 'users/self/media/liked?access_token=%s') % (app_access_token)
    own_media = requests.get(request_url).json()
    if own_media['meta']['code'] == 200:
        if len(own_media['data']):
            print colored("\nSome recent post liked by you:", 'green')
            for ele in own_media['data']:
                print "Username: " + colored(ele['user']['username'], "yellow")
                print "post's url: " + ele['images']["standard_resolution"]["url"]

        else:
            print 'you never liked any post'
            exit()
    else:
        # if access token is wrong an error message gets printed
        print colored(own_media['meta']['error_message'], 'red')
        exit()


def least_like():
    request_url = (base_url + 'users/self/media/recent/?access_token=%s') % (app_access_token)
    own_media = requests.get(request_url).json()
    if own_media['meta']['code'] == 200:
        if len(own_media['data']):
            print colored("\nPost that is least liked by others:",'yellow')
            lst = []
            for ele in own_media['data']:
                lst.append(ele['likes']["count"])
            index = np.argmin(lst)
            print "post's url: " + own_media['data'][index]['images']["standard_resolution"]["url"]
            print "likes: %d"%(min(lst))
        else:
            print 'No post found having least likes'
            exit()
    else:
        # if access token is wrong an error message gets printed
        print colored(own_media['meta']['error_message'], 'red')
        exit()


def like_a_post():
    user_id = friend_id()
    if user_id:
        media_id = get_media_id(user_id)
        request_url = (base_url + 'media/%s/likes') % (media_id)
        payload = {"access_token": app_access_token}
        print 'POST request url is : %s' % (request_url)
        post_a_like = requests.post(request_url, payload).json()
        if post_a_like['meta']['code'] == 200:
            print colored('Like was successful!', 'green')
        else:
            print 'Your like was unsuccessful. Try again!'
    else:
        print colored("Incorrect Username",'red')

def post_a_comment():
    user_id = friend_id()
    if user_id:
        media_id = get_media_id(user_id)
        comment_text = raw_input("Your comment: ")
        payload = {"access_token": app_access_token, "text": comment_text}
        request_url = (base_url + 'media/%s/comments') % (media_id)
        print 'POST request url : %s' % (request_url)
        make_comment = requests.post(request_url, payload).json()
        if make_comment['meta']['code'] == 200:
            print colored("Successfully added a new comment!", "green")
        else:
            print colored("Unable to add comment. Try again!", "red")
    else:
        print colored("Incorrect Username")

def get_list_of_comment():
    user_id = friend_id()
    if user_id:
        media_id = get_media_id(user_id)
        request_url = (base_url + 'media/' + media_id + '/comments?access_token=%s') % (app_access_token)
        comment_list = requests.get(request_url).json()
        if comment_list['meta']['code'] == 200:
            if len(comment_list['data']):
                print colored("\nSome recent comments are", 'green')
                count = 0
                for ele in comment_list['data']:
                    count += 1
                    print "%d.\n comment: " % (count) + colored(ele['text'], "green")
                    print " user name: " + colored(ele['from']["username"], "yellow")
            else:
                print colored('no comment on this post till now', 'green')
                exit()
        else:
            # if access token is wrong an error message gets printed
            print colored(comment_list['meta']['error_message'], 'red')
            exit()
    else:
        print colored("User not found",'red')
