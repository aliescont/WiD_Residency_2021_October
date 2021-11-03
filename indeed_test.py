#resources:https://www.youtube.com/watch?v=PPcgtx0sI2E  


import pandas as pd
from bs4 import BeautifulSoup 
import requests
from requests.api import get
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def get_url(n):
    """Function used for indexing pages given this url as first url 
    https://www.indeed.com/jobs?l=Rancho%20Cordova%2C%20CA&start=0&vjk=44d029cff87a579f
    """
    urls = []
 
    for i in range(n):
        urls.append(f'https://www.indeed.com/jobs?l=Rancho%20Cordova%2C%20CA&start={i*10}&vjk=44d029cff87a579f')
    return urls

def get_info(url):
    headers = {'User Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')


    #print(soup.select('a[id^="job_"]')).get('href')

    title = soup.find_all('h2', attrs={'class': 'jobTitle'})
    titles = [job.find('span', attrs={'title': True}).text for job in title ]

    location = soup.find_all('div', attrs={'class': 'companyLocation'})
    locations = [loc.text for loc in location]

    company = soup.find_all('span', attrs={'class': 'companyName'})
    companies = [c.text for c in company ]
    

    return titles, locations, companies



url = "https://www.indeed.com/jobs?l=Rancho%20Cordova%2C%20CA&start=0&vjk=44d029cff87a579f"


path = "/home/aliciescont/Documents/Github/WiD_Residency_2021_October/chromedriver"    

joblist =  []
urls = get_url(3)



job_titles = []
company_name = []
job_location = []

jobs = dict()
for url in urls:
    page = get_info(url)
    jobs['title'] = page[0]
    jobs['location'] = page[1]
    jobs['company'] = page[2]


df = pd.DataFrame(jobs)
print(df.head())
print(df.shape)
df.to_csv('indeed_job.csv')

