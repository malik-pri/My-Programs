# Creating new 'Hacker News' by scarping web data
# Extracting data based on number of votes received per story and arranged in descending order
# from most voted to least voted; but having more than or equal to 100 votes
import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get("https://news.ycombinator.com/")
soup = BeautifulSoup(res.text, 'html.parser')
res2 = requests.get("https://news.ycombinator.com/news?p=2")
soup2 = BeautifulSoup(res2.text, 'html.parser')

links = soup.select('.titlelink')
subtext = soup.select('.subtext')
links2 = soup2.select('.titlelink')
subtext2 = soup2.select('.subtext')

# connecting page-1 and page-2 news info together
mega_link = links+links2
mega_subtext = subtext+subtext2


def sort_stories_by_votes(hn_list):
    return sorted(hn_list, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for index, item in enumerate(links):
        # print(index, item)
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[index].select('.score')   # for solving the index issue
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({"title": title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)


pprint.pprint(create_custom_hn(mega_link, mega_subtext))

