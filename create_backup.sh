#!/bin/sh

echo "backend: copying files from protected to backup/ "
cp -r /var/www/app/protected/media /var/www/app/backup-data/backend/