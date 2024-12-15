ARG PYTHON_BASE=3.12-slim

# build stage
FROM python:$PYTHON_BASE AS builder

WORKDIR /project

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install PDM
RUN pip install -U pdm
ENV PDM_CHECK_UPDATE=false

COPY pyproject.toml pyproject.toml
COPY pdm.lock pdm.lock

# install dependencies and project into the local packages directory
RUN pdm install --check

# final stage
FROM python:$PYTHON_BASE

WORKDIR /project

COPY --from=builder project/.venv /.venv
ENV PATH=/.venv/bin:$PATH
ENV PYTHONPATH=/project/src

# copy project files to container
COPY ./docker/local/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./docker/local/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

COPY ./docker/local/django/celery/worker/start /start-celeryworker
RUN sed -i 's/\r$//g' /start-celeryworker
RUN chmod +x /start-celeryworker

COPY ./docker/local/django/celery/beat/start /start-celerybeat
RUN sed -i 's/\r$//g' /start-celerybeat
RUN chmod +x /start-celerybeat

COPY ./docker/local/django/celery/flower/start /start-flower
RUN sed -i 's/\r$//g' /start-flower
RUN chmod +x /start-flower


ENTRYPOINT ["/entrypoint"]