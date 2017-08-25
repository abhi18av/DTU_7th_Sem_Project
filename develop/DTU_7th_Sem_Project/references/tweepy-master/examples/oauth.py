from __future__ import absolute_import, print_function

import tweepy

# == OAuth Authentication ==
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumer_key="mZIRcO71flLT1PDaajmHLPaJ9"
consumer_secret="pu1cdINuUfex6OaPoEGEW20Nb0izuO73w0HblyyyJzV20v2cf5"

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located
# under "Your access token")
access_token="3414048620­HZauU3mJwiI7TBrUluFGCPKn4k4UdZviNty6KcD"
access_token_secret="OlZbg7WTAThOnnMHpWKfK82XOKbZ2Sx0Kh082r7uGb3PX"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# If the authentication was successful, you should
# see the name of the account print out
print(api.me().name)

# If the application settings are set for "Read and Write" then
# this line should tweet out the message to your account's
# timeline. The "Read and Write" setting is on https://dev.twitter.com/apps
api.update_status(status='Updating using OAuth authentication via Tweepy!')
