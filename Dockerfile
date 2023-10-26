FROM python:3.8

WORKDIR /var/www/app

COPY . .

RUN pip3 install -r requirements.txt

CMD ["python3", "manage.py", "runserver"]