#!/bin/bash

# 데이터베이스 초기화
flask init-db

# Gunicorn으로 Flask 애플리케이션 실행
exec gunicorn -w 4 -b 0.0.0.0:5000 "app:create_app()"
