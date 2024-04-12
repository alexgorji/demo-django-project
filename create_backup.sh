#!/bin/sh

echo "backend: copying files from protected to backup/ "
mkdir -p /var/www/app/backup-data/backend/
cp -r /var/www/app/protected /var/www/app/backup-data/backend/