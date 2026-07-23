FROM python:3.14-alpine AS base

RUN apk add --no-cache hunspell-dev

FROM base AS runtime

RUN pip install --no-cache-dir dutch-pluralizer && \
    rm -rf \
        /usr/local/lib/python3.14/site-packages/pip* \
        /usr/local/lib/python3.14/site-packages/setuptools* \
        /usr/local/lib/python3.14/site-packages/wheel* \
        /usr/local/bin/pip* \
        /usr/local/bin/idle* \
        /usr/local/bin/pydoc* \
        /usr/local/bin/*.cfg \
        /usr/local/bin/python*-config \
        /usr/include \
        /usr/lib/pkgconfig \
        /usr/share/apk \
        /usr/share/aclocal \
        /usr/share/udhcpc \
        /root/.cache

ENTRYPOINT ["python", "-m", "dutch_pluralizer"]

FROM base AS test

COPY . /build
RUN pip install --no-cache-dir pytest /build && \
    rm -rf \
        /usr/local/lib/python3.14/site-packages/pip* \
        /usr/local/lib/python3.14/site-packages/setuptools* \
        /usr/local/lib/python3.14/site-packages/wheel* \
        /usr/local/bin/pip* \
        /usr/local/bin/idle* \
        /usr/local/bin/pydoc* \
        /usr/local/bin/*.cfg \
        /usr/local/bin/python*-config \
        /usr/include \
        /usr/lib/pkgconfig \
        /usr/share/apk \
        /usr/share/aclocal \
        /usr/share/udhcpc \
        /root/.cache \
        /build

COPY tests /tests
CMD ["python", "-m", "pytest", "/tests"]
