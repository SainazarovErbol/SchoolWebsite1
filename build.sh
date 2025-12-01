#!/usr/bin/env bash
# build.sh

echo "=== Установка зависимостей ==="
pip install --upgrade pip
pip install -r requirements.txt

echo "=== Применение миграций ==="
python manage.py migrate

echo "=== Сбор статических файлов ==="
python manage.py collectstatic --noinput

echo "=== Создание суперпользователя (опционально) ==="
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@example.com', 'admin')"
