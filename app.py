from flask import Flask,render_template
import praw
import os
import datetime
import humanize
from textblob import TextBlob

app = Flask(__name__)

r = praw.Reddit(user_agent='unsentletters/1.0 by /u/icechen1')
def getPost():
    return r.get_random_submission(subreddit='unsentletters')
def sentimentAnalysis(text):
    blob = TextBlob(text)
    return blob.sentiment

@app.route("/")
def home():
    post = getPost()
    sentiment = sentimentAnalysis(post.selftext)
    app.logger.debug(sentiment)
    #app.logger.debug(post.title)
    #app.logger.debug(post.selftext)
    postedTime = humanize.naturaldate(datetime.datetime.fromtimestamp(post.created))
    return render_template('letter.html', post = post, time = postedTime, sentiment = sentiment)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get("PORT", 5000)))
