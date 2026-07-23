FROM python:3.13-alpine AS builder

RUN apk add --no-cache hunspell-dev libffi-dev build-base

COPY . /build
RUN pip install --no-cache-dir --target=/deps /build && \
    rm -rf /deps/pip* /deps/setuptools* /deps/wheel* /root/.cache ~/.cache /build

FROM python:3.13-alpine AS test

RUN apk add --no-cache libhunspell libffi && \
    ln -s libhunspell-1.7.so.0 /usr/lib/libhunspell-1.7.so

ENV PYTHONPATH=/deps
COPY --from=builder /deps /deps
COPY . /build
RUN pip install --no-cache-dir pytest && \
    python -m pytest /build/tests

FROM python:3.13-alpine AS ghcr

RUN apk add --no-cache libhunspell libffi && \
    ln -s libhunspell-1.7.so.0 /usr/lib/libhunspell-1.7.so

COPY --from=builder /deps /deps

ENV PYTHONPATH=/deps
ENTRYPOINT ["python3", "-m", "dutch_pluralizer"]

FROM ghcr AS runtime
