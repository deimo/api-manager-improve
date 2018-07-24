#!/bin/sh
# Author: deimo

cd ..

if [ -d 'deploy/' ]; then
    echo "Error: Directory 'deploy/' is exists."
    exit 1
fi

cp -r deploy.template deploy
cd deploy/
rm -rf genconf.sh
mv template.nginx.conf nginx_api.conf
mv template.supervisor.conf api_manager.conf
mv template.uwsgi.ini uwsgi.ini

exit 0
