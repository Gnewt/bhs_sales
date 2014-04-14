install: bin/python

bin/python:
	. ../bhssales_venv/bin/activate
	../bhssales_venv/bin/pip install -r requirements.txt

serve: bin/python
	bin/gunicorn_start

deploy: bin/python
	../bhssales_venv/bin/python ./manage.py collectstatic --clear --noinput --settings=bhs_sales.settings --configuration=Production
	sudo /var/www/django/bhssales/hup_bhssales
