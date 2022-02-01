import smtplib, ssl
import jinja2
import database_manager as dbms
from datetime import datetime

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import get_cred

port = 465 # Port for SSL
json_dump = get_cred.get()
user_email = json_dump["id"]
password = json_dump["password"] # Passowrd to the gMail Account

# Creating a secure SSL context
context = ssl.create_default_context()

student_srn = ""    # Student SRN
student_name = ""   # Student Name
teacher_name = ""   # Teacher name
query = ""          # Teacher Comment

def send_mail():
# Try to login to server and send email
    try:
        print("Inside try block")
        #  Create a connection to an STMP Server at port 587 (StartTLS)
        server = smtplib.SMTP("smtp.gmail.com", 587) 
        # server.ehlo() # Enable if required
        # Secure the connection
        server.starttls(context = context)
        # server.ehlo() # Enable if required
        # Login to the server
        server.login(user_email, password)
        # Send an email here
        message = MIMEMultipart("alternative")
        message["Subject"] = "Reporting Student"
        message["From"] = str(str(teacher_name) + " <developer.infinitebit@gmail.com>")
        message["To"] = "ujwal2nk@gmail.com"

        part1 = MIMEText(make_mail("plain"), "plain")
        part2 = MIMEText(make_mail("html"), "html")

        message.attach(part1)
        message.attach(part2)

        # server.sendmail(user_email, "rishilghurki07@gmail.com", message.as_string())
        print("Sending mail")
        server.sendmail(user_email, "ujwal2nk@gmail.com", message.as_string())
        print("Mail Sent")

    except Exception as e:
        # Catch and print all exceptions here
        print(e)
    finally: 
        # Close the connection to the server to ensure security
        server.quit()


def make_mail(type):
    global student_srn, student_name, teacher_name, query
    templateLoader = jinja2.FileSystemLoader(searchpath="../include/")
    templateEnv = jinja2.Environment(loader=templateLoader)
    if(type == "html"):
        TEMPLATE_FILE = "html.jinja"
    else:
        TEMPLATE_FILE = "plain-text.jinja"
    template = templateEnv.get_template(TEMPLATE_FILE)
    # this is where to put args to the template renderer
    output_text = template.render({"HOD":"Head of Department", "teacher":teacher_name, "student":student_name, "SRN":student_srn, "time":"11:45AM", "cause":query, "time":datetime.now().strftime("%d %b, %Y %H:%M:%S")}) 
    return output_text

def report(srn, q, teacher):
    print("sending mail")
    global student_srn, student_name, query, teacher_name
    student_srn = srn
    student_name = dbms.get_name(srn, "Student")
    query = q
    teacher_name = teacher
    print(student_name, student_srn, query, teacher)
    send_mail()


