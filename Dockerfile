FROM python:3.11-alpine

WORKDIR /app

COPY . .

COPY requirements.txt /app

RUN pip install -r requirements.txt

ENV PIT_PG_USR=pits
ENV PIT_PG_PWD=burg
ENV PIT_PG_DB=pitsburg
ENV PIT_PG_HOST=pitsburg_db
ENV PIT_PG_PORT=5429
ENV PIT_PG_URI=postgresql+asyncpg://${PIT_PG_USR}:${PIT_PG_PWD}@${PIT_PG_HOST}:${PIT_PG_PORG}/${PIT_PG_DB}

EXPOSE 5000
