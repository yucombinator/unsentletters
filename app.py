from flask import Flask,render_template
import praw
import os
import datetime
import humanize

app = Flask(__name__)

r = praw.Reddit(user_agent='unsentletters/1.0 by /u/icechen1')
def getPost():
    return r.get_random_submission(subreddit='unsentletters')

@app.route("/")
def home():
    post = getPost()

    #app.logger.debug(post )
    #app.logger.debug(post.title)
    #app.logger.debug(post.selftext)
    postedTime = humanize.naturaldate(datetime.datetime.fromtimestamp(post.created))
    return render_template('letter.html', post = post, time = postedTime)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get("PORT", 5000)))
