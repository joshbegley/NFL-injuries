import urllib2
from bs4 import BeautifulSoup
import csv

url = ('http://www.pro-football-reference.com/players/injuries.htm')

page = urllib2.urlopen(url)

soup = BeautifulSoup(page, 'html.parser')
tbody = soup.find('tbody')
injurytable = soup.find(id="all_injuries")
date = [li.text for li in injurytable.find_all('li')]
names = [th.text for th in tbody.find_all('th')]
injuries = [td.text for td in tbody.find_all('td', attrs={"data-stat": "injury_comment"})]

# print date
# print injuries

with open('injuries.csv', 'wb') as f:
	writer = csv.writer(f)
	for dateval in date:
		writer.writerow([dateval])
	for val in names:
		writer.writerow([val])
	for val2 in injuries:
		writer.writerow([val2])
	writer.writerow([injurytable])
