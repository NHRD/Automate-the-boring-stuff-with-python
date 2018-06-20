import requests, bs4

hp_url = input("Input target URL:")
res = requests.get(hp_url)
res.raise_for_status()
res_bs = bs4.BeautifulSoup(res)
hp_list = res_bs.select()