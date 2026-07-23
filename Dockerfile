FROM python:3.13-alpine AS builder

RUN apk add --no-cache hunspell-dev libffi-dev binutils

COPY . /build
RUN pip install --no-cache-dir /build pyinstaller && \
    echo "from dutch_pluralizer.__main__ import main; main()" > /entry.py && \
    pyinstaller --onedir --name pluralizer \
        --add-data "/build/dutch_pluralizer/dict:dutch_pluralizer/dict" \
        --hidden-import cffi \
        --hidden-import pycparser \
        /entry.py && \
    rm -rf /root/.cache ~/.cache /build

FROM python:3.13-alpine AS test

RUN apk add --no-cache hunspell-dev libffi-dev

COPY . /build
RUN pip install --no-cache-dir /build pytest && \
    python -m pytest /build/tests

FROM alpine:3.21 AS runtime

RUN apk add --no-cache libhunspell && \
    ln -s libhunspell-1.7.so.0 /usr/lib/libhunspell-1.7.so

COPY --from=builder /dist/pluralizer /app

WORKDIR /app
ENTRYPOINT ["/app/pluralizer"]

FROM runtime AS ghcr
