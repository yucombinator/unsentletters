from flask import Flask
import praw

app = Flask(__name__)

r = praw.Reddit(user_agent='unsentletters/1.0 by /u/icechen1')
def getPost():
    return r.get_random_submission(subreddit='unsentletters')

@app.route("/")
def home():
    post = getPost()

    #while(len(post)==0):
    #    post = getPost()
    app.logger.debug(post)
    return str(post.selftext)

if __name__ == "__main__":
    app.run(debug=True)
