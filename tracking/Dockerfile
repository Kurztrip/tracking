FROM python:3 as production

ENV PYTHONUNMBUFFERED 1

RUN mkdir /code

RUN apt-get update && \
    apt-get install -y \
    bash \
    build-essential \
    gcc \
    libffi-dev \
    musl-dev \
    openssl \
    postgresql \
    libpq-dev

COPY ./requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt

COPY . /code/

EXPOSE 8000

#CMD ["sh", "-c", "python /code/manage.py makemigrations && python /code/manage.py migrate && python /code/manage.py runserver 0:8000"]