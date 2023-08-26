#!/bin/bash
cd /home/bitnami/api
gunicorn --bind 0.0.0.0:5000 app:app &

cd /home/bitnami/mongodb
npm run dev &

cd /home/bitnami/mysql
python3 -m flask run -p 6000 &

cd /home/bitnami/ml
python3 -m flask run -p 3000 &

# cd D://Arithmetica/core-outline-social-media
# python -m flask run -p 7000 &

wait