import requests
from bs4 import BeautifulSoup

url = 'https://www.cbssports.com/nfl/stats/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

container = soup.find('div', {'class': 'StatsTables'}) 
table = container.find('table') 
tbody = table.find('tbody') 
rows = tbody.find_all('tr') 

print('Top 20 players with the highest number of touchdowns:\n')

for row in rows[:20]:
    data = row.find_all('td')
    player = data[0].text.strip()
    position = data[1].text.strip()
    team = data[2].text.strip()
    touchdowns = data[6].text.strip()
    print(f'{player} ({position}, {team}): {touchdowns} touchdowns')
