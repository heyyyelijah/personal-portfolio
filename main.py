from flask import Flask, render_template, redirect, url_for, request, flash, abort
import requests
from decouple import config
import smtplib

app = Flask(__name__)
url = config('URL')

MY_EMAIL = config('email')
PASSWORD = config('password')

def sendEmail(data):
    data = data.json()
    ip = data['ip']

    if ip != config('my_ip'):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="elijahmamuri@gmail.com",
                msg=f"Subject: PORTFOLIO WAS VIEWED \n\n "
                    f"ip address: {ip}\n"
                    f"country: {data['country_name']}")
    else:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="elijahmamuri@gmail.com",
                msg=f"Subject: you viewed your own portfolio \n\n "
                    f"ip address: {ip}\n"
                    f"country: {data['country_name']}")

@app.route('/')
def home():
    try:
        response = requests.request("GET", url)
        sendEmail(response)
    except:
        pass
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