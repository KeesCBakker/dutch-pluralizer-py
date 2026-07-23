IMAGE_NAME = dutch-pluralizer-dev

.PHONY: test
test:
	docker build -t $(IMAGE_NAME) -f .devcontainer/Dockerfile .
	docker run --rm $(IMAGE_NAME) python -m pytest

.PHONY: test-docker
test-docker:
	docker build --target test .

.PHONY: test-shell
test-shell:
	docker build -t $(IMAGE_NAME) -f .devcontainer/Dockerfile .
	docker run --rm -it $(IMAGE_NAME) bash

.PHONY: build
build:
	docker build -t dutch-pluralizer .
