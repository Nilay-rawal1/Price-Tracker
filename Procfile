web: python manage.py makemigrations && python manage.py migrate && gunicorn PriceTracker.wsgi
celery: celery -A Price_Tracker.celery worker -l info