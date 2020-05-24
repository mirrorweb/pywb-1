.PHONY: env run build clean
.DEFAULT: env

AWS_PROFILE := mw-dmz-dev
SHELL=/bin/bash

# List and check for commands.

COMMANDS = make

COMMAND_CHECK := $(foreach exec,$(COMMANDS), $(if $(shell which $(exec)),some string,$(error "No $(exec) in PATH")))

TAG ?= dev

env:
	@echo "Building the python environment..."
	@python3 -m venv .venv
	@pip install --no-cache-dir -r requirements.txt -r extra_requirements.txt

build:
	@DOCKER_BUILDKIT=1 docker build -t warcserver:${TAG} . --ssh default

run:
	@docker run -v $(pwd)/config.yaml:/opt/mw/config.yaml -p 5005 -it warcserver:${TAG}

clean:
	@rm -rf .venv

