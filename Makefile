CONTAINER_NAME=plactice-service
container-down:
	docker compose down
container-stop:
	docker compose stop
container-exec:
	docker compose exec $(CONTAINER_NAME) bash

# local
local-container-build:
	docker compose -f docker-compose.yml -f docker-compose.local.yml build
local-container-build-no-cache:
	docker compose -f docker-compose.yml -f docker-compose.local.yml build --no-cache
local-container-up:
	docker compose -f docker-compose.yml -f docker-compose.local.yml up -d
local-container-restart:
	make container-down
	make local-container-up

local-run:
	python manage.py runserver

# other
log:
	docker compose logs -f $(CONTAINER_NAME) --tail=100
log-follow:
	docker compose logs -f $(CONTAINER_NAME) --tail=100 --follow