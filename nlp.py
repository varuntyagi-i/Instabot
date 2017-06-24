from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
import requests
from UserId import friend_id
from MediaId import get_media_id
from my_info import base_url,app_access_token
from termcolor import colored

def delete_negative_comment():
    user_id = friend_id()
    if user_id:
        media_id = get_media_id(user_id)
        request_url = (base_url + 'media/%s/comments/?access_token=%s') % (media_id, app_access_token)
        print 'GET request url : %s' % (request_url)
        comment_info = requests.get(request_url).json()

        if comment_info['meta']['code'] == 200:
            if len(comment_info['data']):
                print colored("\nSome recent comments with sentiment analysis", 'green')
                count = 0
                for ele in comment_info['data']:
                    count += 1
                    print "\n%d.\ncomment: " % (count) + colored(ele['text'], "green")
                    blob = TextBlob(ele['text'], analyzer=NaiveBayesAnalyzer())
                    print blob.sentiment
                    if (blob.sentiment.p_neg > blob.sentiment.p_pos):
                        print colored("Negative comment", "red")
                        delete_url = (base_url + 'media/%s/comments/%s/?access_token=%s') % (
                        media_id, ele['id'], app_access_token)
                        print colored('DELETE request url :','red')
                        print ("%s\n" % (delete_url))
                        delete_info = requests.delete(delete_url).json()

                        if delete_info['meta']['code'] == 200:
                            print colored('Comment successfully deleted!', 'green')
                        else:
                            print colored('Unable to delete comment!', 'yellow')
                    else:
                        print colored("Positive comment", 'green')
                    print "user name: " + colored(ele['from']["username"], "green")
            else:
                print colored('no comment on this post till now', 'green')
                exit()
        else:
            # if access token is wrong an error message gets printed
            print colored(comment_info['meta']['error_message'], 'red')
            exit()
    else:
        print colored("Incorrect Username",'red')

