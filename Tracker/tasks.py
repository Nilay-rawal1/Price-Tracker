from django.contrib.auth.models import User
from celery import shared_task
from .models import *
from Scraper import scrape

@shared_task(bind=True)
def GetProductData(self, product_url):
    try:
        data = scrape.getProduct(product_url)
        data_price = int(data.get('price').replace(',', ''))

        product, created = Product.objects.get_or_create(
            name=data.get('name'),
            url=data.get('url'),
            rating = data.get('rating'),
            image_url = data.get('image_url'),
        )

        price_history, created = PriceHistory.objects.get_or_create(
            product=product,
            price=data_price
        )

        if created:
            product.price_history.add(price_history)
            product.save()
        return 'Done'

    except Exception as e:
        raise self.retry(exc=e, max_retries=3)

@shared_task(bind = True)
def AddtoWishlist(self, product_url, user_id):
    user = User.objects.get(id = user_id)
    product_id = Product.objects.get(url = product_url)

    wishlist.objects.create(user = user, product = product_id)
    print(user, product_id)
    return 'Done'

@shared_task
def FetchPrice(bind=True):
    product_list = Product.objects.all()
    count = 0
    for product in product_list:
        data = scrape.parsePrice(product.url)
        data_price = int(data.get('price').replace(',', ''))
        if product.price_history.latest().price != data_price:
            new_price_history = PriceHistory(product=product, price=data_price)
            new_price_history.save()
            product.price_history.add(new_price_history)
            count += 1
        if product.rating != data.get('rating'):
            product.rating = data.get('rating')
            product.save()

    return f'Updated {count} prices'

# iterate through all products
# call scraper to fetch price and rating
# compare if the currently fetched price is same as the most recent price in the database
# if the price is different then add it to the list
# else do nothing
# use bulk create to add all the data to the database
# return the number of prices added and 'Done'