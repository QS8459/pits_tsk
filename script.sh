#!/bin/sh

set -e



echo "Checking if the database is up to date..."
if alembic current | grep -q '(head)'; then
  echo "Database is already up to date. Skipping migrations."
else
  echo "Database is not up to date. Running migrations..."
  alembic revision --autogenerate -m "Init"
  alembic upgrade head
fi


echo "Starting the FastAPI application..."
exec uvicorn src.main:app --host 0.0.0.0 --port 8000 --workers 4