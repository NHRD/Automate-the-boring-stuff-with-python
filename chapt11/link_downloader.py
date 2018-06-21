import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
import random, logging

logging.basicConfig(level = logging.DEBUG, format = "%(asctime)s - %(levelname)s - %(message)s")
logging.debug("program start.")

#logging.disable(logging.DEBUG)

class Link_downloader:

    def __init__(self, hp_url):
        self.hp_url = hp_url
    
    def link_checker(self):
        self.links = []
        r = urllib.request.urlopen(self.hp_url)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser).find_all("a")
        for link in sp:
            self.links.append(link)
        return self.links
    
class Browser_control:

    def __init__(self):
        hp_url = input("Input target URL:")
        browser = webdriver.Firefox()
        self.link_source = Link_downloader(hp_url)
        self.links = self.link_source.link_checker()
        for link in self.links:
            browser.get(link)
 
result = Browser_control()
