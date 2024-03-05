run:
	uvicorn main:app --reload

run_docker:
	systemctl start docker
	sudo docker ps
	docker pull postgres
	docker run --name Users -e POSTGRES_PASSWORD=$1 -d postgres
