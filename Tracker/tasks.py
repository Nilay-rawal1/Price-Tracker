from celery import shared_task
from Scraper import scrape

@shared_task(bind = True)
def GetProdcutData(self, product_url):
    scrape.get(product_url)
    return 'Done'