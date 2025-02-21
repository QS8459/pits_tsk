FROM python:3.11-alpine

WORKDIR /app

COPY . .

COPY requirements.txt /app
COPY script.sh /app

RUN pip install -r requirements.txt
RUN mkdir /app/uploaded
RUN #mkdir alembic
RUN chmod +x script.sh

ENV PIT_APP_TITLE=Pitsburg
ENV PIT_JWT_SECRET_KEY=secretKey
ENV PIT_JWT_ALGORITHM=SH256
ENV PIT_APP_VERSION=0.0.1
ENV PIT_PG_USR=pits
ENV PIT_PG_PWD=burg
ENV PIT_PG_DB=pitsburg
ENV PIT_PG_HOST=pitsburg_db
ENV PIT_PG_PORT=5429
ENV PIT_PG_URI=postgresql+asyncpg://${PIT_PG_USR}:${PIT_PG_PWD}@${PIT_PG_HOST}:${PIT_PG_PORG}/${PIT_PG_DB}

EXPOSE 5000
