#learning beautiful soup

import requests
url = 'https://www.brainyquote.com/topics/motivational-quotes'

r = requests.get(url)
# print(r.content)

from bs4 import BeautifulSoup as bs

soup = bs(r.content, 'html5lib')
# print(soup)

table = soup.find('div', attrs= {'class': 'block-sm bq_on_link_cl'})
print(table)
# print(table.prettify())


# quotes = []
# for row in table.findAll('div', attrs= {'class': 'qti-listm'}):
#     quote = {}
#     try:
#         quote['author'] = row.img(['alt'].split("-")[1])
#         quote['text'] = row.img(['alt'].split("-")[0])
#         quotes.append(quote)

#     except TypeError:
#         continue


# print(quotes)
