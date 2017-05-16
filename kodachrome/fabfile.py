with prefix(VENV):
run('pip install-r requirements.txt > install.log')
run('python manage.py migrate')
