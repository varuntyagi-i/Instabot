from termcolor import colored
from information import friend_info,self_info
from post import get_own_post,get_user_post

def close():
    exit()

while True:
    print colored("\nEnter your choice from the given option:",'blue')
    print "press:\n1.to get your instagram details\n2.to get your friend's instsgram details\n3.to download your most recent most\n" \
          "4.to dowload your friend's most recent post\n5.Close the application"

    choice = int(raw_input())
    dic = {1: self_info,
           2: friend_info,
           3: get_own_post,
           4: get_user_post,
           5: close
           }
    dic[choice]()


