# /blog_project/scripts/commands.sh

#!/bin/sh


set -e

wait_psql.sh
makemigrations.sh
migrate.sh
collectstatic.sh
runserver.sh