import csv
import smtplib
with open('skedar.csv', 'r') as SkedarOrigjinal:
    reader_O = csv.reader(SkedarOrigjinal, delimiter=',')
    with open('skedarStatik.csv', 'r') as Skedari1:
       reader_1 = csv.reader(Skedari1, delimiter=',')
       try:
          a = []
          b = []
          for row1 in reader_O:
             a.append(row1)
             print(type(a))
          for compare_row in reader_1:
             b.append(compare_row)
             print(type(b))
          for item in range(len(a)):
              pass

          for item1 in range(len(b)):
              pass
          if (a[0] == b[0]):

              print('Asgje nuk ka ndryshuar')

          else:
              print('error')

       except IndexError:
           print(" ")






