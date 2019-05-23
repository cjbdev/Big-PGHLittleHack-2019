#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "22867617-2QdXPNw1VirEd48mhZu2080AgGcPFkAI2Y6shsdzT"
access_token_secret = "4UIx5unOHtJ3JYUPC1fBbmbHHdT3suDPxySpoDJo5EDUH"
consumer_key = "VKtY6vPnXZ028bauSSEqAhOnW"
consumer_secret = "rMMXCED5lkBVnZsq31glcgGkjVr0sqlCJ65MEStw8gj83jLnsG"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print (status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['PGHLittleHack'])