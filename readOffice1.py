import csv
import smtplib
with open('skedar.csv', 'r') as SkedarOrigjinal:
    list1 = csv.reader(SkedarOrigjinal, delimiter=',')
    with open('skedarStatik.csv', 'r') as Skedari1:
        list2 = csv.reader(Skedari1, delimiter=',')
        try:
            for row in list1:
                pass
                for row2 in list2:
                    if row[0] == row2[0] and row[1]==row2[1] and row[2] ==row2[2] and row[2]:
                        print('nr nuk kane ndryshuar!')
                    else:
                        print('Te dhenat kane ndryshuar....nje email eshte derguar')

        except IndexError:
            print(" ")







