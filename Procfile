release: python3 -u manage.py runserver 0.0.0.0:8000 && python3 manage.py initadmin
web: python manage.py runserver 0.0.0.0:8000
celery: celery -A login_with_face worker -l INFO -E
