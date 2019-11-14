
from freshmart import app, db
from flask import render_template, redirect, url_for

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/page")
def page():
    return render_template('page.html')

@app.route("/product")
def product():
    return render_template('product.html')

@app.route("/blog")
def blog():
    return render_template('blog.html')

@app.route("/about_us")
def about_us():
    return render_template('about_us.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')


