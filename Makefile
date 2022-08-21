first-setup: build up migrate
up:
	docker-compose up -d
build:
	docker rm -f abex_iv_backend
	docker-compose build
stop:
	docker-compose down
migrate:
	docker exec -it abex_iv_backend python ./abexiv/manage.py makemigrations
	docker exec -it abex_iv_backend python ./abexiv/manage.py migrate
remove-backend: 
	docker stop abex_iv_backend
	docker rm -f abex_iv_backend
remove-db:
	docker stop abex_iv_postgres
	docker rm -f abex_iv_postgres
remove-all: remove-backend remove-db
