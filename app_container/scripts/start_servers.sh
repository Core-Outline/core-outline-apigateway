#!/bin/bash

cd D://Arithmetica/core-outline-apigateway
python -m flask run -p 5000 &

cd D://Arithmetica/core-outline-mongodb-atlas
npm run dev &

cd D://Arithmetica/core-outline-mysql-server
python -m flask run -p 6000 &

cd D://Arithmetica/core-outline-ml-server
python -m flask run -p 3000 &

cd D://Arithmetica/core-outline-social-media
python -m flask run -p 7000 &

wait