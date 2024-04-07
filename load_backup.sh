#!/bin/sh
echo "backend: deleting files inside protected"
rm -rf /var/www/app/protected/*
echo "backend: copying files from backup to protected/ "
cp -r /var/www/app/backup-data/backend/media /var/www/app/protected/