import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
import datetime

#Authorization
auth = tweepy.OAuthHandler(consumer, consumersecret)
auth.set_access_token(access, accesssecret)

api = tweepy.API(auth)

# Declare the name of the file based on the date
currentfile = str(datetime.date.today().day) + str(datetime.date.today().month) + "tweets.txt"

# currentfile = "tweets.txt"

# ensure that the file exists; create if it doesn't
try:
    with(open(currentfile, "r")) as f:
        print("TESTED FILE " + currentfile + " SUCCESSFULLY")
except:
    try:
        with(open(currentfile, "w")) as f:
            f.write(currentfile + "TWEETS FOLLOW \n")
            print("CREATED FILE " + currentfile)
    except:
        print("FILE ERROR ON " + currentfile)

# Where the magic is prepared
class DCIWListener(StreamListener):
    def on_status(self, status):
        if True:
            print(status.text)
            with(open(currentfile, "a")) as f:
                f.write(status.text)
                f.write("|")
                f.write(str(status.user.name))
                f.write('\n')
    def on_error(self, status_code):
        print(str(sys.stderr), 'Encountered error with status code:',str(status_code))
        return True # Don't kill the stream
    def on_timeout(self):
        print(str(sys.stderr), 'Timeout...')
        return True # Don't kill the stream

# Where the magic happens
twitter_stream = Stream(auth, DCIWListener())
twitter_stream.filter(track=["dci2016"])
