import requests
from bs4 import BeautifulSoup

url = 'https://finance.yahoo.com/quote/AAPL/history?p=AAPL'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table', {'class': 'W(100%) M(0)'}) 
tbody = table.find('tbody') 
rows = tbody.find_all('tr') 

print('Apple stock data:\n')

for row in rows:
    data = row.find_all('td')
    date = data[0].text.strip()
    close_price = data[4].text.strip()
    print(f'{date}: {close_price}')
