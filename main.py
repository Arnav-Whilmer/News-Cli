import requests
from bs4 import BeautifulSoup

url = 'https://lite.cnn.com/en'

def function1():

    rawcontent = requests.get(url)
    htmlcontent = rawcontent.content
    parsedcontent = BeautifulSoup(htmlcontent, 'html.parser')
    headlines = parsedcontent.find('ul')
    
    print("\n\n                                 Today's Headlines:\n\n")
    
    for i in headlines:
       print('*', i.text)


function1()

