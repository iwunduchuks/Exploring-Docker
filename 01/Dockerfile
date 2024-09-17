# image: docker/project01:1.0
ARG PYTHON_VERSION=3.12.6

FROM python:${PYTHON_VERSION}

LABEL Maintainer="iwunduchuks@gmail.com" \
      version='1.0' \
      description='docker image for project 01'

WORKDIR /usr/src/app

COPY . .

RUN pwd && ls

ENTRYPOINT [ "python" ]

CMD [ "Hello.py" ]