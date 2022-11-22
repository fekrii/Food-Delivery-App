FROM python:3.10

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
COPY . /app


WORKDIR /app
EXPOSE 8000

RUN pip install --upgrade pip && \
    pip install -r /requirements.txt && \
    adduser --disabled-password --no-create-home app && \
    mkdir -p /home/app/web && \
    mkdir -p /home/app/web/staticfiles && \
    mkdir -p /home/app/web/mediafiles && \
    chown -R app:app /home/app/web && \
    chmod -R 755 /home/app/web


ENV PATH="/py/bin:$PATH"

USER app

# CMD ["run.sh"]