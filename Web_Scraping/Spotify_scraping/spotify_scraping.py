from bs4 import BeautifulSoup
import pandas as pd
import requests
from time import sleep
from datetime import date, timedelta

'''
*Beautiful Soup helps us to extract data from HTML files.
*Pandas will help us transform our array of data (one-dimensional, hard to read, disorganized) 
 into a nice data-frame (two-dimensional, easy-to read).
*Requests allows us to send HTTP requests, allowing us to get relevant info from the webpages, 
 such as content, encoding, etc.
*Sleep makes sure that we don’t overwhelm the server by sending too many requests at once.
 It puts a pause in our code. This also helps to make sure our page is fully loaded before proceeding.
*Date will help us tack on dates to our base URL so that we can get top daily song data. 
Timedelta will help us to get data for each day in the duration which we’re studying.
'''

dates = []
url_list = []
final = []

url = 'https://spotifycharts.com/regional/us/daily/'
start_date = date(2021, 1, 1)
end_date = date(2022, 1, 1)
delta = end_date-start_date
# print(delta)
# print(delta.days)


for i in range(delta.days+1):
    day = start_date + timedelta(days=i)
    day_string = day.strftime("%Y-%m-%d")
    # print(day, day_string)
    dates.append(day_string)


# creating a function to update all urls per date
def add_url():
    for date in dates:
        new_string = url+date
        url_list.append(new_string)


add_url()


def song_scrape(get_url):
    for tr in songs.find(name='tbody').find_all(name='tr'):
        artist = tr.find(name='td', attrs={'class': 'chart-table-track'}).find('span').text
        artist = artist.replace('by', '').strip()
        title = tr.find(name='td', attrs={'class': 'chart-table-track'}).find('strong').text
        songid = tr.find(name='td', attrs={'class': 'chart-table-image'}).find('a').get('href')
        songid = songid.split('track/')[1]
        url_date = get_url.split('daily/')[1]
        final.append([title, artist, songid, url_date])


for i in url_list:
    page = requests.get(i)
    print(page)
    sleep(2)
    soup = BeautifulSoup(page.text, 'html.parser')
    songs = soup.find('table', {'class': 'chart-table'})
    print(songs)
    song_scrape(i)


final_df = pd.DataFrame(final, columns=['Title', 'Artist', 'Song Id', 'Chart Date'])

with open('spotify_top200.csv', 'w') as f:
    final_df.to_csv(f, header=True, index=False)



