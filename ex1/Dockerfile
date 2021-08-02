FROM python:latest

USER root

RUN useradd -u 1001 michaelgrn
WORKDIR /home/michaelgrn

RUN python -m venv venv \
    && chown -R michaelgrn /home/michaelgrn

USER michaelgrn

RUN . venv/bin/activate

COPY --chown=michaelgrn app/ /code/app

WORKDIR /code

RUN python -m pip install -e /code/app

CMD python -m app
