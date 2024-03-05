create_docker_container:
	docker run --name XDrive -p 5432:5432 -e POSTGRES_PASSWORD=secret -e POSTGRES_USER=arthur -d postgres

create_postgres_db:
	docker exec -it XDrive createdb --username=arthur --owner=arthur users

start_docker:
	docker start XDrive

stop_docker:
	docker stop XDrive
