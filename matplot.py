from wordcloud import WordCloud

import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
from UserId import friend_id
from my_info import base_url,app_access_token
from termcolor import colored
import requests

def interest():
    user_id = friend_id()
    if user_id:
        request_url = (base_url + 'users/' + user_id +'/media/recent/?access_token=%s') % (app_access_token)
        caption = requests.get(request_url).json()
        if caption['meta']['code'] == 200:
            if len(caption['data']):
                print colored("\nSome recent post with cation: ", 'green')
                count = 0
                caption_list = []
                for ele in caption['data']:
                    count += 1
                    if ele['caption'] == None:
                        print '%d\n '%(count) + colored('no caption','yellow')
                        caption_list.append('post with no caption')
                    else:
                        print "%d.\n caption: " % (count) + colored(ele['caption']['text'], "green")
                        caption_list.append(ele['caption']['text'])

                    print " post url: " + colored(ele['images']['standard_resolution']['url'], "yellow")

#display all values with there frequency in list and store it in counts(i.e. dictionary)
                counts = Counter(caption_list)
#use to plot graph on the basis of hashtag analysis of user
                wordcloud = WordCloud().generate_from_frequencies(counts)
                plt.imshow(wordcloud,interpolation='bilinear')
                plt.axis("off")
                plt.show()
#print the frequecy of each hashtag
                print '\n'
                for ele in counts:
                    print "%s : %d"%(ele,counts[ele])

                """
                caption_list_count = []
                for value in caption_list:
                    caption_list_count.append(caption_list.count(value))
                print len(caption_list_count)
                print caption_list_count
                print caption_list

                x = np.arange(len(caption_list_count))
                plt.bar(x, height = caption_list_count)
                plt.xticks(x+1,caption_list)
                plt.plot([1, 2, 3], [1, 2, 3])
                """
            else:
                print colored('no post till now: ', 'yellow')
                exit()
        else:
            # if access token is wrong an error message gets printed
            print colored(caption['meta']['error_message'], 'red')
            exit()
    else:
        print colored("User not found", 'red')


