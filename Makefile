IMAGE_NAME = dutch-pluralizer

.PHONY: test
test:
	docker build -t $(IMAGE_NAME)-dev -f .devcontainer/Dockerfile .
	docker run --rm $(IMAGE_NAME)-dev python -m pytest

.PHONY: test-shell
test-shell:
	docker build -t $(IMAGE_NAME)-dev -f .devcontainer/Dockerfile .
	docker run --rm -it $(IMAGE_NAME)-dev bash

.PHONY: docker
docker:
	docker build -t $(IMAGE_NAME) .

.PHONY: docker-push
docker-push:
	docker buildx create --name multiarch --use --bootstrap 2>/dev/null || true
	docker buildx build \
		--platform linux/amd64,linux/arm64 \
		-t $(IMAGE_NAME) \
		--push \
		.

.PHONY: docker-push-ghcr
docker-push-ghcr:
	docker buildx create --name multiarch --use --bootstrap 2>/dev/null || true
	docker buildx build \
		--platform linux/amd64,linux/arm64 \
		-t ghcr.io/keescbakker/dutch-pluralizer:latest \
		--push \
		.
