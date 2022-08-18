up:
	docker-compose up
build:
	docker-compose build

migrate:
	docker exec -it abexiv-backend_server_1 python ./abexiv/manage.py makemigrations
	docker exec -it abexiv-backend_server_1 python ./abexiv/manage.py migrate