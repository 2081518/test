FROM python:3.5-alpine3.8
MAINTAINER Thor Marinho

# Setting up the directory that will be used
WORKDIR /home/

# Setting up the ENTRYPOINT
COPY docker-production/start /home/
RUN chmod u+x /home/start

COPY requirements.txt /home
COPY src /home/src/

# Software Development kit for alpine
RUN apk add --update alpine-sdk

# Python setup
RUN cd /usr/bin \
  && ln -sf easy_install-3.5 easy_install \
  && ln -sf idle3.5 idle \
  && ln -sf pydoc3.5 pydoc \
  && ln -sf python3.5 python \
  && ln -sf python3.5-config python-config \
  && ln -sf pip3 pip3

# Install pip3
RUN apk upgrade --no-cache \
  && pip3 install --no-cache-dir --upgrade pip

# Cryptography Library of Python3, basic configs
RUN apk add openssl-dev
RUN apk add libffi-dev

# Alpine basics
RUN apk --no-cache --update add build-base
RUN apk add --no-cache  openssh-client
RUN apk add autoconf
Run apk add pkgconfig
RUN apk add --update libxml2-dev libxslt-dev
RUN apk add libtool

# Setup of pip3
RUN if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi

# Installing dependencies of the project
RUN pip3 install -r requirements.txt && \
    pip3 install service_identity --force --upgrade

# Removing the cache
RUN rm -r /root/.cache

# Alpine basics
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV XDG_RUNTIME_DIR=/tmp/runtime-root

# Just the ENTRYPOINT
ENTRYPOINT /home/start
