# -*-coding: utf-8-*-
import json
import codecs
import foursq_profiles
import foursq_tips
import foursq_friends
import random
import pymongo

#sys_api_token = 0
#sys_client_version = 0
min_id = 1
max_id = 532419618
total_user = 0
valid_user = 0
users_with_tips = 0
users_w_tips = 0

myclient = pymongo.MongoClient('127.0.0.1', 27017)
mydb = myclient["f4q_crawler"]
mycol = mydb["users"]

def get_json(user_id):
    global users_w_tips
    crawl_tips = {}
    crawl_tips['user info'] = foursq_profiles.fetch_user_profile(user_id)
    if crawl_tips['user info'] != -1:
        crawl_tips['tips'], users_w_tips = foursq_tips.fetch_usr_tips(user_id)
        crawl_tips['friends'] = foursq_friends.fetch_usr_friends(user_id)
    else:
        return -1
    return crawl_tips

def bfs(centerUID,upperbound):
    global valid_user
    global users_with_tips
    global users_w_tips
    queueUID = [str(centerUID)]
    visitedUID =[]
    output_file = codecs.open("4sq_tips_chunk_friends_of_%d.json" % (centerUID), "w", "utf-8-sig")
    visitedUID_file = codecs.open("visitedUID.json","w","utf-8-sig")
    error_file = codecs.open("invalidUID.json", "a" "utf-8-sig")
    # unvisitedUID_file = codecs.open("Unvisited UID","w","utf-8-sig")

    for UID in queueUID:
        result = get_json(str(UID))
        if result != -1:
            visitedUID.append(UID)
            print (UID, 'Done')
            output_file.write("%s\n" % result)
            visitedUID_file.write("%s\n" % UID)
            x = mycol.insert_one(result)
            valid_user = valid_user + 1
            users_with_tips = users_with_tips + users_w_tips
            friendsUID = result['friends']['friendsUID']
            duplicateUID = list(set(friendsUID).intersection(set(queueUID)))
            addUID = [x for x in friendsUID if x not in duplicateUID]
            queueUID.extend(addUID)

            # for y in queueUID:
            #     if y not in visitedUID:
            #         unvisitedUID_file.write("%s\n" % y)
        else:
            error_file.write(str(UID)+"\n")

        if valid_user >= upperbound:
            break

if __name__ == '__main__':
    bfs(123456,1000)
    print ("valid_user: " , valid_user)
    print ("users_with_tips: " , users_with_tips)
