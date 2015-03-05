
'''
MinneapolisFact Twitter Bot
This is a short script that will randomly grab a line from a textfile and post
it to Twitter. Feel free to use this for your own Twitter bot.

To use this, hook it up to a cronjob. Since this outputs what it's going to
tweet, pipe stdout to a log file. 

You will need to have a file named 'facts.txt' which contains the tweets to
post, each on it's own line. You will also need to fill in the OAuthSettings.py
file with your Twitter app credentials. 

Requires the Python Twitter library:
	- https://github.com/bear/python-twitter
'''

from OAuthSettings import settings
import random
import twitter

def random_line(afile):
    line = next(afile)
    for num, aline in enumerate(afile):
      if random.randrange(num + 2): continue
      line = aline
    return line


tweet = random_line(open('facts.txt'))
print tweet

try:
	api = twitter.Api(
	consumer_key = settings['consumer_key'],
	consumer_secret = settings['consumer_secret'], 
	access_token_key = settings['access_token_key'], 
	access_token_secret = settings['access_token_secret'])
	
	status = api.PostUpdate(tweet)				# this does the actual posting!
	print 'post successful!'

except twitter.TwitterError:
	print 'error posting!'

exit()
