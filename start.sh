#!/bin/bash

function err_handling() {
    if [ $? -ne 0 ]; then
        echo "[ $BASH_COMMAND ] section is faild"
        echo "Error: $1"
        exit 1
    fi
}
trap 'err_handling $LINENO' ERR

cd app
poetry run python manage.py runserver 0:8000