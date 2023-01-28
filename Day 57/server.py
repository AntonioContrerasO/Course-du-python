from flask import Flask,render_template
import random
import datetime
import requests

app = Flask(__name__)



@app.route('/')
def home():
    random_number = random.randint(1,10)
    year = datetime.datetime.now().year
    print(year)
    return render_template("index.html",random_number=random_number,year=year)

@app.route('/guess/<name>')
def guess(name):
    response_gender = requests.get(f'https://api.genderize.io?name={name}')
    gender = response_gender.json()['gender']
    response_age = requests.get(f'https://api.agify.io?name={name}')
    age = response_age.json()['age']
    return render_template("plantilla.html",name=name.capitalize(),gender=gender,age=age)

@app.route('/blog/<num>')
def get_blog(num):
  print(num)
  blog_url="https://api.npoint.io/be862485d98f339fb9eb"
  response = requests.get(blog_url)
  all_posts = response.json()
  return render_template("blog.html",posts=all_posts)
if __name__=="__main__":
    app.run(debug=True)