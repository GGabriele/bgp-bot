.PHONY: build_image
build_image:
	docker import cEOS-lab.tar.xz ceosimage:4.20.5F

.PHONY: commands
commands:
	bash commands.sh

.PHONY: up
up:
	docker-compose up -d
	sleep 60
	bash commands.sh

.PHONY: down
down:
	docker-compose down
