# /blog_project/scripts/commands.sh

#!/bin/sh

set -e

while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
    echo "⏳ Waiting for Postgres Database Startup ($POSTGRES_HOST $POSTGRES_PORT) ..."
    sleep 2
done

echo "✅ Postgres Database Started Successfully ($POSTGRES_HOST $POSTGRES_PORT) ..."

collectstatic.sh ## # /blog_project/scripts/collectstatic.sh
makemigrations.sh ## # /blog_project/scripts/makemigrations.sh
migrate.sh ## # /blog_project/scripts/migrate.sh
runserver.sh ## # /blog_project/scripts/runserver.sh