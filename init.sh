#!/bin/bash

python -m venv ./venv
./venv/bin/pip install -r requirements.txt
echo "Пропиши:"
echo ". venv/bin/activate"
echo "Заполни конфиг: config.py"
echo "python main.py - запуск"