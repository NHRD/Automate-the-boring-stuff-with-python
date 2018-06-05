#! python3

import requests, sys, webbrowser, bs4, pyperclip

if len(sys.argv) > 1:
    key = " ".join(sys.argv[1:])
else:
    key = pyperclip.paste()

pnum = int(input("Input page number to brows.:"))
print("Googling...")
res = requests.get("http://google.com/search?q=" + key)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text)
link_elems = soup.select(".r a")

num_open = min(pnum, len(link_elems))
for i in range(num_open):
    webbrowser.open("http://google.com" + link_elems[i].get("href"))
if pnum == 1:
    print("I'm feeling lucky..")