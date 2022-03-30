import pandas as pd
from bs4 import BeautifulSoup
import requests

top250 = []
url = 'https://www.imdb.com/chart/top/'

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
table = soup.find('table', {'class': 'chart full-width'})

for tr in table.find('tbody', {'class': 'lister-list'}).find_all('tr'):
    movie = tr.find('td', {'class': 'titleColumn'}).text.split('\n')[2].strip()
    temp = tr.find('td', {'class': 'titleColumn'}).find('a').get('title')
    director = temp.split('(dir.),')[0]
    cast = temp.split('(dir.),')[1]
    year = tr.find('td', {'class': 'titleColumn'}).find('span', {'class': 'secondaryInfo'}).text.strip('()')
    rating = tr.find('td', {'class': 'ratingColumn imdbRating'}).text.strip('\n')
    top250.append([movie, director, cast, year, rating])

top250list = pd.DataFrame(top250, columns=['Movie', 'Director', 'Cast', 'Year', 'Rating'])
print(top250list)
