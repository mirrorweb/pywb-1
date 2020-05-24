# syntax=docker/dockerfile:experimental
FROM python:3.8-slim-buster AS vanilla_base_image
LABEL maintainer="Mark Johnson 'mark.johnson@mirrorweb.com'"
LABEL version="0.0.1"
LABEL description="A container for warcserver, a webarchive api"

# Install gcc :(
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc g++ python3-dev make git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Setup the python env
ENV VIRTUAL_ENV=/opt/mw/.venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install requirements
COPY requirements.txt extra_requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt -r extra_requirements.txt

COPY . ./
RUN python setup.py install

# Vanilla Delorian with no external modules
FROM python:3.8-slim-buster AS vanilla_image
WORKDIR /opt/mw
# Setup the python env
ENV VIRTUAL_ENV=/opt/mw/.venv
COPY --from=vanilla_base_image /opt/mw/.venv .venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

CMD mkdir collections/{full-zipnum,staging-zipnum}

COPY config.yaml ./config.yaml
COPY pywb ./pywb

ENTRYPOINT warcserver -b 0.0.0.0 -p 5005 --debug
