from flask import Flask, render_template, redirect, url_for, request, flash, abort
import requests
from emails import sendEmail
from decouple import config

app = Flask(__name__)
url = config('URL')


@app.route('/')
def home():
    response = requests.request("GET", url)

    sendEmail(response)
    return render_template("index.html", home_page=True)

@app.route('/projects')
def projects():
    return render_template("projects.html", projects_page=True)

@app.route('/about')
def about():
    return render_template("about.html", about_page=True)

@app.route('/contact')
def contact():
    return render_template("contact.html", contact_page=True)

@app.route('/tindog')
def tindog():
    return render_template("tindog.html")

if __name__ == "__main__":
    app.run(debug=True)