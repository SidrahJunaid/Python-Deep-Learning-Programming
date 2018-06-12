import  urllib.request
from  bs4 import  BeautifulSoup
import  os

link="https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"

source_code=urllib.request.urlopen(link)
soup=BeautifulSoup(source_code,"html.parser")

# find table of specific class
body = soup.find('table', {'class': 'wikitable sortable plainrowheaders'})
# find all rows in the class
table_row=body.find_all('tr')

# find td and th iin the rows
for tr in table_row:
    td=tr.find_all('td')
    print(td)
    th=tr.find_all('th')
    print(th)

# title of page
print(soup.title.string)

# find all anchor tag
print(soup.find_all('a'))

# find href attribute in anchor tag
for url in soup.find_all('a'):
    print(url.get('href'))

