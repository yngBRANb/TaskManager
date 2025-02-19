FROM python:3.11

WORKDIR /app


RUN pip install --no-cache-dir django

COPY . .
RUN python manage.py makemigrations
RUN python manage.py migrate


CMD [ "python", "manage.py", "runserver", "0.0.0.0:8080" ]