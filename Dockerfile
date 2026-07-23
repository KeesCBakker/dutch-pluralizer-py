FROM python:3.14-slim AS builder

RUN apt-get update && apt-get install -y --no-install-recommends \
    libhunspell-dev \
    && rm -rf /var/lib/apt/lists/*

COPY . /build
RUN pip install --no-cache-dir /build

FROM python:3.14-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    libhunspell-1.7-0 \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /usr/local /usr/local

ENTRYPOINT ["python", "-m", "dutch_pluralizer"]
