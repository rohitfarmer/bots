#!/usr/bin/env python3

# Standar library.
import os
import time

# External non pip installed library.
from src import InstaBot
from src.check_status import check_status
from src.feed_scanner import feed_scanner
from src.follow_protocol import follow_protocol
from src.unfollow_protocol import unfollow_protocol

# OAuth authentication.
with open('../../cred/exp_insta.txt', 'r') as f: # Reading the credentials from a text file.
    creds = f.readlines()
    login = creds[0].rstrip()
    password = creds[1].rstrip()

bot = InstaBot(login, password,
               like_per_day=1000,
               media_max_like=50,
               media_min_like=5,
               tag_list=['travel','adventure','wanderlust','vacation','travelgram','explore','holiday','travels','traveler','traveller','traveling','travelling','travelphotography','mobilephotography','architecture', 'travelingram','travelblog','travelblogger','traveladdict','exploretocreate','passionpassport','tourism','mytravelgram','instapassport','tourist','traveltheworld', 'instagood','food','sweet','yummy','instapic','yum','delicious','fresh','foodie','homemade', 'foodporn', 'foodie', 'mountain','beautifuldestinations','life','runner','hike','naturephotography','picoftheday','beauty','roadtrip','gopro','discover','climbing','camping','naturelovers','trekking','holiday'],
               max_like_for_one_tag=50,
               log_mod=1)

while True:

    #print("# MODE 0 = ORIGINAL MODE BY LEVPASHA")
    #print("## MODE 1 = MODIFIED MODE BY KEMONG")
    #print("### MODE 2 = ORIGINAL MODE + UNFOLLOW WHO DON'T FOLLOW BACK")
    #print("#### MODE 3 = MODIFIED MODE : UNFOLLOW USERS WHO DON'T FOLLOW YOU BASED ON RECENT FEED")
    #print("##### MODE 4 = MODIFIED MODE : FOLLOW USERS BASED ON RECENT FEED ONLY")
    #print("###### MODE 5 = MODIFIED MODE : JUST UNFOLLOW EVERYBODY, EITHER YOUR FOLLOWER OR NOT")

    ################################
    ##  WARNING   ###
    ################################

    # DON'T USE MODE 5 FOR A LONG PERIOD. YOU RISK YOUR ACCOUNT FROM GETTING BANNED
    ## USE MODE 5 IN BURST MODE, USE IT TO UNFOLLOW PEOPLE AS MANY AS YOU WANT IN SHORT TIME PERIOD

    mode = 0

    #print("You choose mode : %i" %(mode))
    #print("CTRL + C to cancel this operation or wait 30 seconds to start")
    #time.sleep(30)

    if mode == 0:
        bot.new_auto_mod()

    elif mode == 1:
        check_status(bot)
        while bot.self_following - bot.self_follower > 200:
            unfollow_protocol(bot)
            time.sleep(10 * 60)
            check_status(bot)
        while bot.self_following - bot.self_follower < 400:
            while len(bot.user_info_list) < 50:
                feed_scanner(bot)
                time.sleep(5 * 60)
                follow_protocol(bot)
                time.sleep(10 * 60)
                check_status(bot)

    elif mode == 2:
        bot.bot_mode = 1
        bot.new_auto_mod()

    elif mode == 3:
        unfollow_protocol(bot)
        time.sleep(10 * 60)

    elif mode == 4:
        feed_scanner(bot)
        time.sleep(60)
        follow_protocol(bot)
        time.sleep(10 * 60)

    elif mode == 5:
        bot.bot_mode = 2
        unfollow_protocol(bot)

    else:
        print("Wrong mode!")