web: python manage.py migrate && gunicorn PriceTracker.wsgi
worker: celery -A Price_Tracker.celery worker -l INFO