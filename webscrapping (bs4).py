import requests
from bs4 import BeautifulSoup

urls = open("urls", "r").read().splitlines()


def get_table(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    table = soup.find('table', attrs={'class': 'tableagmark_new'})
    rows = table.find_all('tr')

    with open('20-21_Oct_2021/ ' + market + '.csv', 'w') as f:
        for row in rows:
            cols = row.find_all('th')
            cols = [ele.text.strip() for ele in cols]
            f.write(",".join(cols) + " " + "\n")
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            f.write(",".join(cols) + " ")


for i in urls:
    market = i.split("Tx_MarketHead=")[1]
    get_table(i)
