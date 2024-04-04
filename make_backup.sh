#!/bin/sh

echo "backend: copying files from protected to backup/files "
cp -r /var/www/app/protected/. /var/www/app/backup/files/