#!/usr/bin/env bash
cd ~/projects/kasaverde
. venv/bin/activate
. ./.env
date >> /var/log/verde.log
python main.py >> /var/log/verde.log

