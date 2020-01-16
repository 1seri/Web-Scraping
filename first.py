import csv
import requests
from bs4 import BeautifulSoup
URL = 'https://w3development.net'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
contact = soup.find( id = 'footer')
#print(contacts.prettify())
file = open('skedar.csv', 'w')
writer = csv.writer(file)
phone = soup.find_all('span', {'class':'phone text-2'})
for i in phone:
    links = i.find_all('a')
    for link in links:
        print(link.text)
#aksesimi i emailit
email = soup.find_all('span', {'class': 'footer-email-custom float-right'})
for n in email:
    links = n.find_all('a')
    for link1 in links:
        print(link1.text)
writer.writerow([link.text, link1.text])
file.close()
