FROM python:3

ENV PYTHONUNMBUFFERED 1

RUN mkdir /code

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY . /code/

EXPOSE 8000

CMD ["sh", "-c", "python /code/manage.py makemigrations && python /code/manage.py migrate && python /code/manage.py runserver 0:8000"]