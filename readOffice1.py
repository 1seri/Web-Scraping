import csv
from email.mime.text import MIMEText
import smtplib
#!/usr/bin/env python
def send_email():
    sender = "from@smtp.mailtrap.io"
    receiver = "to@smtp.mailtrap.io"
    msg = MIMEText('This is test mail')
    msg['Subject'] =('Test mail')
    msg['From'] = 'from@smtp.mailtrap.io'
    msg['To'] = 'to@smtp.mailtrap.io'
    user = '984f98daf98eb1'
    password = '5aee14525c9521'

    with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
        server.login(user, password)
        server.sendmail(sender, receiver, msg.as_string())
        print("mail successfully sent")

with open('skedar.csv', 'r') as SkedarOrigjinal:
    list1 = csv.reader(SkedarOrigjinal, delimiter=',')
    with open('skedarStatik.csv', 'r') as Skedari1:
        list2 = csv.reader(Skedari1, delimiter=',')
        try:
            for row in list1:
                pass
                for row2 in list2:
                    pass
                    if (row[0]==row2[0] and row[1]==row2[1] and row[2]==row2[2] and row[3]==row2[3] and row[4]==row2[4] and row[5]==row2[5] and
                        row[6]==row2[6] and row[7]==row2[7] and row[8]==row2[8] and row[9]==row2[9] and row[10]==row2[10] and row[11]==row2[11]
                        and row[12]==row2[12] and row[13]==row2[13] and row[14]==row2[14] and row[15]==row2[15]):
                        print('data has not changed :)!')


                    else:
                        send_email()

        except IndexError:
            print(" ")













