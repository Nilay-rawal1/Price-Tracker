from Scraper.Spiders.AmazonSpider import *

def getProduct(url):
    return parseProduct(url)

def getPrice(url):
    return parsePrice(url)