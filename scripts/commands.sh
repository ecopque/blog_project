# /blog_project/scripts/commands.sh

#!/bin/sh

set -e #14:

while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
    echo "Waiting for Postgres Database Startup ($POSTGRES_HOST $POSTGRES_PORT) ..."
    sleep 0.1 ##
done ##

echo "Postgres Database Started Successfully ($POSTGRES_HOST $POSTGRES_PORT) ..."

python3 manage.py collectstatic
python3 manage.py migrate
python3 manage.py runserver