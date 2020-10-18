python3 -m venv imgvenv 		# Создаем виртуальное окружение
source imgvenv/bin/activate 		# Переходим в виртуальное окружение
python3 -m pip install --upgrade pip 	# Обновляем загрузчик зависимостей
pip3 install -r requirements.txt 	# Обновляем зависимости
python3 manage.py makemigrations 	# Создаем миграцию в БД
python3 manage.py migrate 		# Проводим миграцию в БД
python3 manage.py collectstatic 	# Обновляем статичные файлы
python3 manage.py createsuperuser 	# Создаем суперюзера
python3 manage.py runserver 		# Запускаем сервер
