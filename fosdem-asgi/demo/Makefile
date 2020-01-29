install:
	pip install -r requirements.txt

runserver:
	python manage.py runserver

daphne:
	daphne demo.asgi:application

migrate:
	python manage.py migrate

runworker:
	python manage.py runworker thumbnails-generate

tests:
	python manage.py test
