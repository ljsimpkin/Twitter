import tweepy
import passwords
from textblob import TextBlob

# Step 1 - Authenticate
consumer_key = passwords.key
consumer_secret = passwords.secret

access_token = passwords.token
access_token_secret = passwords.token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#Step 3
since_date = '2018-03-01'
until_date = '2018-04-18'
search = 'realDonaldTrump'
count =	100

public_tweets = api.user_timeline(search, count = count)

polarity = ''
text = []
sentiment = []
sentiment_value = []
date = []
time = []
retweets = []
follower_count = []
likes = []
reply_count = []
location = []
url = []
#coordinates = []
i = 0

for tweet in public_tweets:
	analysis = TextBlob(tweet.text)
	number = analysis.sentiment[0]
	if number == 0:
		polarity = 'neutral'
	elif number > 0:
		polarity  = 'positive'
	else:
		polarity = 'negative'
	text.append(tweet.text)
	sentiment.append(polarity)
	sentiment_value.append(number)
	date_time = str(tweet.created_at)
	split = date_time.split()
	date.append(split[0])
	time.append(split[1])
	retweets.append(tweet.retweet_count)
	likes.append(tweet.favorite_count)
	#follower_count.append(tweet.user.followers_count)
	#location.append(tweet.user.location)
	#url.append('https://twitter.com/' + str(tweet.user.screen_name) + '/status/' + tweet.id_str)

download_dir = "trump.csv"
csv = open(download_dir, "w")

columnTitleRow = "Time, Date, Sentiment Value, Sentiment, Retweets, Likes\n"
csv.write(columnTitleRow)

while i < count:
	csv.write('%s,%s,%s,%s,%s,%s\n' % (time[i], date[i], sentiment_value[i], sentiment[i], retweets[i], likes[i]))
	i = i + 1
