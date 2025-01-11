#!/bin/bash
set -e

create_env_file() {
    if [ ! -f .env ]; then
        echo "Creating .env file from environment variables..."
        : ${SERVICE:=""}
        : ${USERNAME:=""}
        : ${PASSWORD:=""}
        : ${CHECK_INTERVAL:=300}

        echo "SERVICE=\"$SERVICE\"" > .env
        echo "USERNAME=\"$USERNAME\"" >> .env
        echo "PASSWORD=\"$PASSWORD\"" >> .env
        echo "CHECK_INTERVAL=$CHECK_INTERVAL" >> .env
    fi
}

create_env_file

exec "$@"