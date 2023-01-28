import smtplib
from flask import Flask, render_template, request
import requests

response = requests.get("https://api.npoint.io/721faac2b50d46718866")
data = response.json()
ids = []
bodys = []
titles = []
subtitles = []

for i in range(len(data)):
    ids.append(data[i].get("id"))
    bodys.append(data[i].get("body"))
    titles.append(data[i].get("title"))
    subtitles.append(data[i].get("subtitle"))



app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html",ids=ids,titles=titles,subtitles=subtitles)
@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact' , methods = ["GET","POST"])
def contact():
    if request.method == "GET":
        return render_template("contact.html")
    if request.method == "POST":

        passwordG = "Ivan1234"
        my_email = "idiomas51231@gmail.com"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=passwordG)
            connection.sendmail(from_addr=my_email, to_addrs="antonio61231@gmail.com",
                                msg=f"Subject:Monday\n\n Name: {request.form['name']}\n"
                                    f"Email: {request.form['email']}\n"
                                    f"Phone: {request.form['phone']}\n"
                                    f"Message: {request.form['msg']}")
        send = "SUCESSFULLY SENT YOUR MESSAGE"
        return render_template("contact.html",send=send)

@app.route('/post/<int:id>')
def post(id):
    return render_template("post.html",id=id,titles=titles,subtitles=subtitles,bodys=bodys)


if __name__ == "__main__":
    app.run(debug=True)