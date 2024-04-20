#!/bin/sh

echo "backend: creating backup-data/backend if not exists"
mkdir -p /var/www/app/backup-data/backend

echo "backend: cleaning backup-data/backend"
rm -rf /var/www/app/backup-data/backend/*

echo "backend: copying files from protected to backup-data/backup/ "
cp -r /var/www/app/protected /var/www/app/backup-data/backend/