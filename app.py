from flask import Flask,render_template
import praw

app = Flask(__name__,port=int(os.environ.get("PORT", 5000)))

r = praw.Reddit(user_agent='unsentletters/1.0 by /u/icechen1')
def getPost():
    return r.get_random_submission(subreddit='unsentletters')

@app.route("/")
def home():
    post = getPost()

    #while(len(post)==0):
    #    post = getPost()
    app.logger.debug(post)
    app.logger.debug(post.title)

    return render_template('letter.html', title = post.title, text=post.selftext)

if __name__ == "__main__":
    app.run(debug=True)
