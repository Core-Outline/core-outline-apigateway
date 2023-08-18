#!/bin/bash
cd /home/ubuntu/api
gunicorn --bind 0.0.0.0:5000 app:app &

cd /home/ubuntu/mongodb
npm run dev &

cd /home/ubuntu/mysql
python3 -m flask run -p 6000 &

cd /home/ubuntu/ml
pyt -m flask run -p 3000 &

# cd D://Arithmetica/core-outline-social-media
# python -m flask run -p 7000 &

wait