import requests
import random

from scrapy import Selector
from Scraper.headers import user_agents

def fetch_data(url):
    headers = {
        'User-Agent': random.choice(user_agents)
    }
    response = requests.get(url, headers = headers)
    return response

def parseProduct(url):
    response = fetch_data(url)
    item = {}
    if response.status_code == 200:
        html = response.text
        selector = Selector(text=html)

        url = url
        name = selector.css('span.a-size-large.product-title-word-break::text').get().strip()
        
        
        try:
            rating = selector.css('span.a-icon-alt::text').get().replace(' out of 5 stars', '')
        except:
            rating = None

        if selector.css('img.a-dynamic-image.a-stretch-vertical'):
            image_url = selector.css('img.a-dynamic-image.a-stretch-vertical').attrib['src']
        else:
            image_url = selector.css('img.a-dynamic-image.a-stretch-horizontal').attrib['src']
        
        try:
            price = selector.css('span.a-price-whole::text').get().replace(',', '')
        except:
            price = None
        
        item = {
            'domain': 'Amazon',
            'url': url,
            'name': name,
            'price': price,
            'rating': rating,
            'image_url': image_url,
        }

    return item

def parsePrice(url):
    response = fetch_data(url)

    if response.status_code == 200:
        html = response.text
        selector = Selector(text=html)

        try:
            rating = selector.css('span.a-icon-alt::text').get().replace(' out of 5 stars', '')
        except:
            rating = None

        try:
            price = selector.css('span.a-price-whole::text').get()
        except:
            price = None

        item = {
            'price': price,
            'rating': rating,            
        }
        return item
    else:
        return None
    