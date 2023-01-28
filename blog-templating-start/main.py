import requests
from flask import Flask, render_template

app = Flask(__name__)

blog_url = "https://api.npoint.io/be862485d98f339fb9eb"
response = requests.get(blog_url)
all_posts = response.json()


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


@app.route('/blog/<int:num>')
def get_blog(num):
    post = all_posts[num]
    print(post)
    return render_template("post.html", posts=post)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
