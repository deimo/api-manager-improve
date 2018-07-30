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

cp ../api_manager/dev_settings.py.template ../api_manager/dev_settings.py
cp ../api_manager/prod_settings.py.template ../api_manager/prod_settings.py
exit 0
