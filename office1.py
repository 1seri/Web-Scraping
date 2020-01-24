import config
import csv
import requests
from bs4 import BeautifulSoup
page = requests.get(config.URL)
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
headers = {'User-Agent': user_agent}
response = requests.get(config.URL,headers=headers)
html= response.content
soup = BeautifulSoup(response.content, 'html.parser')
#print(response.content)

contacts = soup.find('div',id ='footer2-left')
phone = soup.find_all('ul',{'class':'phone-list'})
list_nr =[]
for i in phone:
    links = soup.find_all('li', {'class':'phone-list-number'})
    for link in links:
        list_nr.append(link.text)
file = open('skedar.csv', 'w')
writer = csv.writer(file)
writer.writerow(list_nr)
print(list_nr)



