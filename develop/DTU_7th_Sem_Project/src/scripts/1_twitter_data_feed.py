from tweepy import Stream 
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey='pD6v5kfp67FXY2NASfowDazRJ'
csecret='7iZO2rFiMDUwOqOfQVJF4RfVxbQtoapQ1eTMUeFs1e8szTaDVy'

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located
# under "Your access token")
atoken='3414048620-HZauU3mJwiI7TBrUluFGCPKn4k4UdZviNty6KcD'
asecret='OlZbg7WTAThOnnMHpWKfK82XOKbZ2Sx0Kh082r7uGb3PX'

# Tweepy

class listener(StreamListener):
    def on_data (self, data):
        print(data)
        return True
        
    def on_error(self, status):
        print(status)
        
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)


import time 

start_time = time.time()
ls = []
while True:
    twitterStream = Stream(auth, listener())
    ls.append(twitterStream.filter(track = ["car"]))
    
    if(( time.time() - start_time ) < 0.009):
           break