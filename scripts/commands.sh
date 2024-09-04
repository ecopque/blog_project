#!/bin/sh

# /blog_project/scripts/commands.sh

set -e

wait_psql.sh # /blog_project/scripts/wait_psql.sh
makemigrations.sh # /blog_project/scripts/makemigrations.sh
migrate.sh # /blog_project/scripts/migrate.sh
collectstatic.sh # /blog_project/scripts/collectstatic.sh
runserver.sh # /blog_project/scripts/runserver.sh