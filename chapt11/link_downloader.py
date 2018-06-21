import requests, bs4
from selenium import webdriver

def link_checker(hp_url):
    links = []
    res = requests.get(hp_url)
    res.raise_for_status()
    res_bs = bs4.BeautifulSoup(res.text)
    hp_list = res_bs.select("#list h2 a")
    for i in range(len(hp_list)):
        links.append(hp_list[i].get("href"))
    return links

def hp_opener(links):
    browser = webdriver.Firefox()
    for link in links:
        browser.open(link)

def main():
    hp_url = input("Input target URL:")
    hp_opener(link_checker(hp_url))
