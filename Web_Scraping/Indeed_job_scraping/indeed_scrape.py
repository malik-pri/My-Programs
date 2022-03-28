import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import pprint

url = 'https://www.indeed.com/jobs?q=data%20scientist%20%2420%2C000&l=New%20York&start=10&vjk=a1cf96c5fb53ee2f'

# conducting a request of the stated URL above:
res = requests.get(url)
# specifying a desired format of “page” using the html parser-
# this allows python to read the various components of the page,
# rather than treating it as one long string.
soup = BeautifulSoup(res.text, 'html.parser')

# printing soup in a more structured tree format that makes for easier reading
soup.prettify()


def extract_job_title(soup):
    jobs = []
    for div in soup.find_all(name='div', attrs={'class': 'job_seen_beacon'}):
        for h2 in div.find_all(name='h2', attrs={'class': 'jobTitle'}):
            # print(h2)
            # pprint.pprint(h2.text)
            jobs.append(h2.text)
    return jobs


def extract_company_name(soup):
    company = []
    for div in soup.find_all(name='div', attrs={'class': 'job_seen_beacon'}):
        for span in div.find_all(name='span', attrs={'class': 'companyName'}):
            a = span.find(name='a', attrs={'class': 'turnstileLink'})
            # print(a)
            #         # print(a)
            if a:
                company.append(a.text)
            else:
                company.append(span.text)
    return company


def extract_company_location(soup):
    location = []
    for div in soup.find_all(name='div', attrs={'class': 'job_seen_beacon'}):
        for div2 in div.find_all(name='div', attrs={'class': 'companyLocation'}):
            # print(div2.text)
            location.append(div2.text)
    return location


def extract_salary(soup):
    salary = []
    for div in soup.find_all(name='div', attrs={'class': 'job_seen_beacon'}):
        # print(div.text)
        try:
            for div2 in div.find_all(name='div', attrs={'class': 'metadata salary-snippet-container'}):
                # print(div2.text)
                salary.append(div2.text.strip())
            for span in div.find_all(name='span', attrs={'class': 'estimated-salary'}):
                # print(span.text)
                salary.append(span.text.strip())
        except:
            salary.append('N/A')
    return salary


def extract_job_summary(soup):
    summary = []
    for div in soup.find_all(name='div', attrs={'class': 'job_seen_beacon'}):
        for div2 in div.find_all(name='div', attrs={'class': 'job-snippet'}):
            # print(div2.text)
            summary.append(div2.text.strip())
    return summary


pprint.pprint(extract_job_title(soup))
pprint.pprint(extract_company_name(soup))
pprint.pprint(extract_company_location(soup))
pprint.pprint(extract_salary(soup))
pprint.pprint(extract_job_summary(soup))






