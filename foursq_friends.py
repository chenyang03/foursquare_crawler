import json
from foursq_utils import *

def fetch_usr_friends(user_id):
    super_token = 'QEJ4AQPTMMNB413HGNZ5YDMJSHTOHZHMLZCAQCCLXIX41OMP'
    url = 'https://api.foursquare.com/v2/users/' + str(user_id) + '/friends?oauth_token=' + super_token + '&v=20210115'
    try:
        raw = get_raw_info(url)
        data = json.loads(raw)
        if data['meta']['code'] != 200:
            return -1
        friends_info = data['response']['friends']
        friendsUID = []
        if 'items' in friends_info.keys():
            for item in friends_info['items']:
                friendsUID.append(item['id'])
            friends_info.setdefault('friendsUID',friendsUID)
        else:
            friends_info.setdefault('friendsUID', [])
        return friends_info

    except:
        return -1


