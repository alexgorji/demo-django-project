#!/bin/sh

echo "backend: copying files from protected to backup/ "
cp -r /var/www/app/protected/. /var/www/app/backup/