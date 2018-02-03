from termcolor import colored
from information import friend_info,self_info
from post import get_own_post,get_user_post,recent_like,least_like,like_a_post,post_a_comment,get_list_of_comment
from nlp import delete_negative_comment
from matplot import interest

def close():
    exit()

while True:
    print colored("\nEnter your choice from the given option:",'blue')
    print "press:\n1.to get your instagram details\n2.to get your friend's instsgram details\n3.to download your most recent Post\n" \
          "4.to dowload your friend's most recent post\n5.Get to know about the post having least likes. \n6.Most recent post liked by me.\n" \
          "7.to like friend's post\n8.get list of comment from a post\n9.to post a comment on someone's post\n10.to delete negative comments o" \
          "n a post \n11.to determine a user's interests and plot the same.\n12.Close the application"

    choice = int(raw_input())
    dic = {1: self_info,
           2: friend_info,
           3: get_own_post,
           4: get_user_post,
           5: least_like,
           6: recent_like,
           7: like_a_post,
           8: get_list_of_comment,
           9: post_a_comment,
           10: delete_negative_comment,
           11: interest,
           12: close
           }
    dic[choice]()


