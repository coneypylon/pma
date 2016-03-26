import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
import datetime

auth = tweepy.OAuthHandler("nInlDnZsePX4wPkDkzx2xv4Nr", "VJpzpe6rMYEE4qG6QI4ARNH4j4sOvHttnpeUoDAeGNawWfv28m")
auth.set_access_token("3862054103-VY7yn3ygT4zLOvX9dgA6aV4NztFzASBgDkiwWG2", "a4uMZZLdOPZwGf4AC1YwbiTFGb62msVA77CTTui2XP8tQ")

api = tweepy.API(auth)

currentfile = str(datetime.date.today().day) + str(datetime.date.today().month) + "tweets.txt"

# currentfile = "tweets.txt"

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

keywords = ['Academy', 'The Academy', 'Blue Devils', '#dci', '@dci', '@DCI', 'Blue Knights', 'Knights', 'Blue Stars', 'Stars', 'Bluecoats', 'Bloo', 'Boston Crusaders', 'Boston', 'The Cadets', 'Cadets', 'cadets', 'the cadets', 'Carolina Crown', 'Carolina', 'Crown', 'Cascades', 'The Cavaliers', 'Cavaliers', 'Colts', 'Crossmen', 'Jersey Surf', 'Surf', 'Madison Scouts', 'The Scouts', 'Mandarins', 'Oregon Crusaders', 'Pacific Crest', 'Crest', 'Phantom Regiment', 'Phantom', 'Pioneer', 'Santa Clara Vanguard', 'SCV', 'Spirit of Atlanta', 'Troopers']

twitter_stream = Stream(auth, DCIWListener())
twitter_stream.filter(track=["dci2016"])
