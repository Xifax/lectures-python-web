test:
	ptw tasks/tests.py -- --testmon

run:
	python manage.py runserver

clean:
	rm lessons/db.sqlite3
	rm tasks/migrations/*.py
	python manage.py makemigrations
	python manage.py migrate
	python manage.py createsuperuser --username admin --noinput

