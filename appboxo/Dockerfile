FROM python:3
COPY . /usr/src/app
WORKDIR /usr/src/app

ENV SECRET_KEY=Some-Generated-Secret-Key
ENV DATABASE_URL=sqlite:///db.sqlite3
ENV REDIS_CACHE_URL=redis://redis:6379/1
ENV DEBUG=False

RUN touch .env
RUN printenv > .env
RUN pip install -r requirements.txt

RUN python manage.py migrate