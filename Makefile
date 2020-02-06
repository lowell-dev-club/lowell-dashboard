init:
	pip3 install -r requirements.txt
	
update:
	pip install --upgrade alembic bcrypt blinker cffi Click Flask Flask-Bcrypt Flask-login Flask-Mail Flask-Migrate Flask-SQLAlchemy Flask-wtf itsdangerous jinja2 mako markupsafe pillow pip pycparser pystarter python-dateutil python-editor setuptools six SQLAlchemy Werkzeug wheel WTForms
	pip freeze > requirements.txt

clean:
	pystarter clean

run: clean
	python3 run.py