include ./.env
export $(shell sed 's/=.*//' ./.env)

local: cleanup start add_conns add_vars

restart: local-stop local

local-stop: 
	@echo "Stopping Airflow local environment"
	docker-compose down -v
	
start:
	@echo "Starting Airflow local environment"
	@echo "http://localhost:8080/admin"
	docker-compose up -d

add_conns:
	@echo "Adding Reddit Connection to Airflow"
	@docker-compose run --rm scheduler \
		airflow connections --delete \
			--conn_id reddit_api > /dev/null || true
	@docker-compose run scheduler \
		airflow connections --add \
			--conn_id reddit_api \
			--conn_type http \
			--conn_login ${REDDIT_USERNAME} \
			--conn_password ${REDDIT_USERNAME} \
			--conn_extra ${REDDIT_EXTRA}

add_vars:
	@echo "Adding example variable"
	@docker-compose run scheduler \
		airflow vairables --set \
			variable_key 'variable value'

cleanup: 
	@echo "Cleaning up environment"
	@docker-compose rm -f

build:
	@docker build -t dangkv/docker-airflow:latest .
