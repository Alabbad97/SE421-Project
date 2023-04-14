from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")

def hello():
    return "Hello World!"

app.run(debug=True)

from json import dumps
from postdata import posts

@app.route("/json_posts")
def json_posts():
    data= {
        'data' : posts,
        'total' : len(posts)
    }
    return dumps(data)

@app.errorhandler(404)
def err_404(error):
    return render_template( '404.html' ), 404

@app.route("/mobileswith data")
def mobiles():
    return render_template('mobiles.html',
    title = 'My Home page',
    posts = posts )
