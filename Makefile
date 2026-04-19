DC = docker compose
EXEC = docker compose exec
MAIN_FILE = docker-compose.yml
APP_CONTAINER = backend


.PHONY: all
all:
	${DC} -f ${MAIN_FILE} up -d

.PHONY: bash
bash:
	${EXEC} ${APP_CONTAINER} bash
