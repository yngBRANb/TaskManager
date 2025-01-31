# TaskManager

##Clear install

<code>pip install --no-cache-dir django
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8080</code>

##Install with docker

<code>docker build -t taskmanager .
docker run -p 8080:8080 -d taskmanager
</code>

##Create superuser in docker

<code>docker exec -it <container name> bash
python manage.py createsuperuser      
</code>
