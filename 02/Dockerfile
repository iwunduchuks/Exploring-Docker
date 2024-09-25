# image: docker/project02:1.0
ARG PYTHON_VERSION=3.12.6

FROM python:${PYTHON_VERSION}

LABEL Maintainer="iwunduchuks@gmail.com" \
      version='1.0' \
      description='docker image for project 02'

ENV LOAD_ROUTE='database'

WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt

RUN pwd && ls

ENTRYPOINT [ "python" ]

CMD [ "pipline_main.py" ]