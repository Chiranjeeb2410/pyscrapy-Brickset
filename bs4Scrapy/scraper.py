import urllib.request
from bs4 import BeautifulSoup

quote_page  = 'https://www.bloomberg.com/quote/SPX:IND'
res_page = urllib.request.urlopen(quote_page)
quote_res = BeautifulSoup(res_page, 'html.parser')

title_box = soup.find_all('span', attrs={'class': 'companyName'})
name =  title_name.text.strip()
print (name)

time_stamp  = soup.find('span', attrs={'id': 'quote_dateTime', 'class': 'timestamp_value'})
time  = time_stamp.text.strip()
print (time)

price_val = soup.find('span', attrs={'id': 'quote_val'})
price = price_val.text.strip()
print (price)

quote_change = soup.find('span', attrs={'id': 'quote_change', 'class': 'cr_num diff_price'})
change = quote_change.text.strip()
print (change)

quote_changeCent = soup.find('span', attrs={'id': 'quote_changePer', 'class': 'cr_num diff_percent'})
changeCent = quote_changeCent.text.strip()
print (change)
