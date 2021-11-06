import smtplib
from decouple import config

MY_EMAIL = config('email')
PASSWORD = config('password')

def sendEmail(data):
    data = data.json()
    ip = data['ip']

    if ip != config('my_ip'):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="elijahmamuri@gmail.com",
                msg=f"Subject: PORTFOLIO WAS VIEWED \n\n "
                    f"ip address: {ip}\n"
                    f"country: {data['country_name']}")
    else:
        print(ip)