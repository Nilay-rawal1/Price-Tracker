import requests
from Scraper.Spiders import ProductDetailsSpider 

def FindDomain(url):
    domain = url.replace("http://", "").replace("https://", "").replace("www.", "").replace(".com", "").replace(".in", "").split("/")[0]
    return domain

def amazon_link(url):
    clean_step1 = url.split('?')[0]
    link = clean_step1.split("/")
    r = ''
    for i in link:
        if len(i) == 10:
            r = 'https://www.amazon.in/dp/' + i
            break
    return r
    
def flipkart_link(url):
    link = url.split('?')[0]
    return link
    
def not_supported(url):
    return f"The given {url} is not supported"

domain_function_mapping = {
    'amazon': amazon_link,
    'flipkart': flipkart_link,
}

def url_valid(url):
    try:
        response = ProductDetailsSpider.fetch_data(url)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException:
        return False

def clean_url(url):
    domain = FindDomain(url)
    link_cleaner = domain_function_mapping.get(domain, not_supported)
    new_link = link_cleaner(url)
    return new_link