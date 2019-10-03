import datetime
import tweepy
import json
import time
import emoji
from tweepy.error import TweepError

access_token = "...."
access_token_secret = "...."
consumer_key = "...."
consumer_secret = "...."
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)
original_tweet=0
filtered_count=0
def extract_tweets(poi,max_id,id_lis,original_tweet):
    try:
        filtered_count=0
        poi_tweet_file = poi + 'newtweets.json'
        end_encountered = 0
        any_tweet_found = True;
        while(original_tweet < 1800 and any_tweet_found ):
            
            any_tweet_found = False
            if max_id == 0:
                print("Default call")
                cur = tweepy.Cursor(api.user_timeline, screen_name=poi, tweet_mode='extended').items(2000)
            else:
                print("Max Id call")
                cur = tweepy.Cursor(api.user_timeline, screen_name=poi,max_id = max_id-1 , tweet_mode='extended').items(2000)
            for tweet in cur:
                 
                 max_id = tweet.id
               
                 if not hasattr(tweet, 'retweeted_status') and not tweet.in_reply_to_status_id:
                    any_tweet_found = True


                    if original_tweet >=1800:
                      break
                   
                    original_tweet+=1
                   
                    if tweet.created_at > min_date and tweet.created_at < max_date:
                        filtered_count+=1
                        id_lis.append(tweet.id)
                        print(tweet.id)
                    with open(poi_tweet_file, 'a+', encoding="utf8") as f:
                        obj = convertToObj(tweet)
                        print(obj["tweet_date"])

                        json.dump(obj, f, ensure_ascii=False)
    except TweepError as e:
        time.sleep(10)
        print(e)
        extract_tweets(poi,max_id,id_lis,)


def extract_replies(poi,id_list,replies_lis,replies_count_map,max_id):
    try:
        poi_replies_file = poi + 'newreplies.json'
        i =0;
        since_id = min(id_list)
        total_tweets = 0
        last_max_id = max_id
        extraction_finished = 0;
        while (1):
            if max_id == 0:
                cur = tweepy.Cursor(api.search, q='to:'+poi, since_id=since_id, count=1000,tweet_mode='extended').items(1000)
            else:
                cur = tweepy.Cursor(api.search, q='to:'+poi, since_id=since_id, max_id=max_id-1,count=1000,tweet_mode='extended').items(1000)
            for tweet in cur:
                max_id = tweet.id
                if tweet.in_reply_to_status_id in id_list:
                    total_tweets = total_tweets+1
                    if len(replies_count_map[tweet.in_reply_to_status_id]) <= 20:
                        replies_lis.append(tweet)
                        obj = convertToObj(tweet)
                        obj["poi_name"] = poi
                        obj["poi_id"] = obj["replied_to_user_id"]
                        replies_count_map[tweet.in_reply_to_status_id].append(obj)
                        if last_max_id == max_id or all(len(v) >= 20 for v in replies_count_map.values()):

                break
       
    except TweepError:
       time.sleep(10)
       extract_replies(poi,id_list,replies_lis,replies_count_map,max_id)

def round_to_hour(dt):
    dt_start_of_hour = dt.replace(minute=0, second=0, microsecond=0)
    dt_half_hour = dt.replace(minute=30, second=0, microsecond=0)

    if dt >= dt_half_hour:
        # round up
        dt = dt_start_of_hour + datetime.timedelta(hours=1)
    else:
        # round down
        dt = dt_start_of_hour

    return dt

def get_place_obj(place):
    objec = {}
    objec['country_code'] = place.country_code
    objec['coordinates'] = place.bounding_box.coordinates
    objec['name'] = place.name
    return objec

def convertToObj(tweet):
    obj={}
    obj["poi_name"] = tweet.user.screen_name
    obj["poi_id"] = tweet.user.id
    obj["verified"] = tweet.user.verified
    obj["country"] = "India"
    obj["replied_to_tweet_id"] = tweet.in_reply_to_status_id_str
    obj["replied_to_user_id"] = tweet.in_reply_to_user_id_str
    if tweet.in_reply_to_user_id:
        obj["reply_text"] = tweet.full_text
    obj["tweet_text"] = tweet.full_text
    obj["tweet_lang"] = tweet.lang
    obj["hashtags"] = tweet.entities["hashtags"]
    obj["mentions"] = tweet.entities["user_mentions"]
    obj["tweet_urls"] = tweet.entities["urls"]
    obj["retweeted"] = tweet.retweeted
    if not tweet.place is None:
        obj["tweet_loc"] = get_place_obj(tweet.place)
    obj["id"] = tweet.id
    obj["retweet_count"] = tweet.retweet_count
    obj["favorite_count"] = tweet.favorite_count
    obj["favorited"] = tweet.favorited
    obj["tweet_emoticons" ] = ''.join(c for c in tweet.full_text if c in emoji.UNICODE_EMOJI)
    obj["tweet_date"] = str(round_to_hour(tweet.created_at))
    return obj

min_date = datetime.datetime(2019, 9, 7)
max_date = datetime.datetime(2019, 9, 12)
poi = 'BDUTT'
poi_tweet_file = poi + 'newtweets.json'
poi_replies_file = poi + 'newreplies.json'
id_list = []
extract_tweets(poi,0,id_list,0)
time.sleep(1)
replies_list=[]
count_map = {}
print(len(id_list))
for id in id_list:
    count_map[id] = []
extract_replies(poi,id_list,replies_list,count_map,0)
with open(poi_replies_file, 'a+', encoding="utf8") as f:
    for id in id_list:
        for obj in count_map[id]:
             json.dump(obj, f, ensure_ascii=False)          
  
time.sleep(1)
print('Original count', original_tweet)
