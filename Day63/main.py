from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# import sqlite3
#
# db = sqlite3.connect("books-collection.db")
#
# cursor = db.cursor()
#
# # cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
#
# cursor.execute("INSERT INTO books VALUES(6768, 'Potter 2556', 'J. K. Rowling', '9.3')")
# db.commit()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


@app.route('/',methods=["GET","POST"])
def home():
    if request.method == "POST":
        book_to_delete = Books.query.get(request.args.get('id'))
        db.session.delete(book_to_delete)
        db.session.commit()
        redirect("url_for('home')")
    if request.method == "GET":
        all_books = db.session.query(Books).all()
        return render_template("index.html", books=all_books)


@app.route("/add")
def add():
    return render_template("add.html")

@app.route("/delete")
def delete():
    book_id = request.args.get('id')
    # DELETE A RECORD BY ID
    book_to_delete = Books.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/edit", methods=["GET", "POST"])
def edit():
    id = request.args.get('id')
    book = Books.query.filter_by(id=id).first()
    if request.method == "GET":
        return render_template("edit.html",book=book)
    if request.method == "POST":
        rating = request.form['rating']
        book.rating = rating
        db.session.commit()
        return redirect(url_for('home'))



if __name__ == "__main__":
    app.run(debug=True)
