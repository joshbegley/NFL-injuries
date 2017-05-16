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
injury_type = [td.text for td in tbody.find_all('td', attrs={"data-stat": "injury_type"})]
status = [td.text for td in tbody.find_all('td', attrs={"data-stat": "injury_class"})]
team = [td.text for td in tbody.find_all('td', attrs={"data-stat": "team"})]
position = [td.text for td in tbody.find_all('td', attrs={"data-stat": "pos"})]
blank = " "

# print date
# print injuries

row1 = zip(date,blank,blank,blank,blank,blank)
rows = zip(names,injuries,injury_type,status,team,position)

with open('injuries.csv', 'wb') as f:
	writer = csv.writer(f)
	#for dateval in date:
	#	writer.writerow([dateval])
	for row in row1:
		writer.writerow(row)
	for row in rows:
		writer.writerow(row)
