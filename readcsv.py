import csv
import smtplib
with open('skedar1.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter = ',')
    try:
        for row in readCSV:
            if row[0] =='+355 (0) 69 3858 950' and row[1] == 'info [at] w3development [dot] net':
                print('Numri i kontaktit dhe emaili, nuk kane ndryshuar!')
            else:
                print('Te dhenat kane ndryshuar....nje email eshte derguar')

    except IndexError:
            print(" ")

sender = "Private Person <from@smtp.mailtrap.io>"
receiver = "A Test User <to@smtp.mailtrap.io>"

message = f"""\
Subject: Hi Mailtrap
To: {receiver}
From: {sender}

Seri this works thanks God."""

with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
    server.login("984f98daf98eb1", "5aee14525c9521")
    server.sendmail(sender, receiver, message)


