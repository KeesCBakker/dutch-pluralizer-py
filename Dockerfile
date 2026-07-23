FROM python:3.14-alpine AS builder

RUN apk add --no-cache hunspell-dev gcc musl-dev libffi-dev

COPY . /build
RUN pip install --no-cache-dir /build

FROM python:3.14-alpine

RUN apk add --no-cache hunspell-dev

COPY --from=builder /usr/local /usr/local

ENTRYPOINT ["python", "-m", "dutch_pluralizer"]
