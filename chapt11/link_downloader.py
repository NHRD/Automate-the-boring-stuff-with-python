import requests, bs4
from selenium import webdriver

def link_checker(hp_url):
    links = []
    res = requests.get(hp_url)
    res.raise_for_status()
    res_bs = bs4.BeautifulSoup(res)
    hp_list = res_bs.select("#list h2 a")
    for i in hp_list:
        links.append(i.get("href"))
    return links

def hp_opener(link):
    browser = webdriver.Firefox()

hp_url = input("Input target URL:")