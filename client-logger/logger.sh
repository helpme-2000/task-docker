#!/bin/bash
while true; do
    echo "$(date): Отправка циклического запроса к веб-приложению..."
    # curl стучится к первому контейнеру по его имени в сети Docker
    curl -s http://web-app:8080/
    echo -e "\n-------------------------"
    sleep 5
done
