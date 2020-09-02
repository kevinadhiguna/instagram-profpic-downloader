import requests
from bs4 import BeautifulSoup

username = input("What's the username of account? : ")
url = 'https://instagram.com/{}/'

r = requests.get(url.format(username))
s = BeautifulSoup(r.text, 'html.parser')
u = s.find('meta', property='og:image')
url = u.attrs['content']

with open(username+'.jpg','wb') as pic:
    binary = requests.get(url).content
    pic.write(binary)
