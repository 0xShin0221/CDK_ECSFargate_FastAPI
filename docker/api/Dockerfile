# Use the official Python image.
# https://hub.docker.com/_/python
FROM python:3.7

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    ca-certificates \
    git \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ENV WORKDIR /usr/src/server/

WORKDIR ${WORKDIR}

COPY Pipfile Pipfile.lock ${WORKDIR}

RUN set -ex \
    && apt-get update -y --fix-missing \
    && apt-get install -y -q --no-install-recommends \
    curl \
    file \
    && apt-get purge -y --auto-remove


RUN pip install pipenv --no-cache-dir && \
    pipenv install --system --deploy && \
    pip uninstall -y pipenv virtualenv-clone virtualenv

COPY backend $WORKDIR

CMD ["uvicorn", "main:api", "--host", "0.0.0.0", "--port", "8080"]