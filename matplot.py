from wordcloud import WordCloud

import matplotlib.pyplot as plt
# import numpy as np
from collections import Counter
from UserId import friend_id
from my_info import base_url,app_access_token
from termcolor import colored
import requests

def interest():
    user_id = friend_id()
    if user_id:
        request_url = (base_url + 'users/' + user_id +'/media/recent/?access_token=%s') % (app_access_token)
        hashtag = requests.get(request_url).json()
        if hashtag['meta']['code'] == 200:
            if len(hashtag['data']):
                print colored("\nSome recent post with hashtags: ", 'green')
                count = 0
                tags_list = []
                for ele in hashtag['data']:
                    count += 1
                    if ele['tags'] == []:
                        print '\n%d\n '%(count) + colored('no hashtag','yellow')
                        #tags_list.append('')
                    else:
                        print "\n%d"%(count)
                        for tag in range(0,len(ele['tags'])):
                            print "tags: " + colored(ele['tags'][tag], "green")
                            tags_list.append(ele['tags'][tag])

                    print " post url: " + colored(ele['images']['standard_resolution']['url'], "yellow")

                if len(tags_list) > 0:
                    # contains all values with there frequency in tags_list list and store it in counts(dictionary)
                    # note: return typr of Counter is dictionary
                    counts = Counter(tags_list)
                    # use to plot graph on the basis of hashtag analysis of user
                    wordcloud = WordCloud().generate_from_frequencies(counts)
                    plt.imshow(wordcloud, interpolation='bilinear')
                    plt.axis("off")
                    plt.show()

                    # print the frequecy of each hashtag
                    print '\n'
                    for ele in counts:
                        print "%s : %d" % (ele, counts[ele])

                else:
                    print colored("no hashtag on user's post",'red')

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
            print colored(hashtag['meta']['error_message'], 'red')
            exit()
    else:
        print colored("User not found", 'red')


