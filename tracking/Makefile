build:
	sudo docker build $(options) -t tracking .

compose:
	sudo docker-compose up --remove-orphans $(options)

compose-stop:
	sudo docker-compose down --remove-orphans $(options)

compose-manage-py:
	sudo docker-compose run --rm $(options) website python /code/manage.py $(cmd)
