import json
import sys


if len(sys.argv) != 3: 
    print "usage python hashcount.py \"#HashTag\" YYYY"
    exit(-1)
hashtag = sys.argv[1]
if hashtag[0] == "#":
    hashtag = hashtag[1:]
tweet_yr = sys.argv[2]
hash_count = 0
loaded_tweets = [];

for i in range(1,13):
#    print "processing month: %d" %(i)
    try:
        js_file = open("data/js/tweets/%s_%02d.js" %(tweet_yr, i))
    except IOError:
        print "no file for month %d" %(i)
        continue
    loaded_tweets = json.load(js_file)
    for tweet in loaded_tweets:
        hashtags = tweet["entities"]["hashtags"]
        if any( hashtag.lower() in tag["text"].lower() for tag in hashtags):
            hash_count += 1
    js_file.close()

print "\n#%s happened %d times in the year %s!!" %(hashtag, hash_count, tweet_yr)
