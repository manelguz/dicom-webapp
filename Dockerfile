FROM python:3.8

RUN apt update && apt install npm -y

# File Author / Maintainer
MAINTAINER Manel

#add project files to the usr/src/app folder
ADD dicom-viewer /app

#set directoty where CMD will execute 
WORKDIR /app

# Get pip to download and install requirements:
RUN pip install --no-cache-dir -r requirements_docker.txt

ARG azure_name # you could give this a default value as well
ARG azure_key
ARG django_key

ENV AZURE_ACCOUNT_NAME=$azure_name 
ENV AZURE_ACCOUNT_KEY=$azure_key
ENV SECRET_KEY=$django_key

RUN cd frontend/ && npm install && npm run-script build
#RUN python manage.py makemigrations && python manage.py migrate && 
RUN python manage.py collectstatic

# Expose ports
EXPOSE 8080

# default command to execute    
CMD exec gunicorn core.wsgi:application --bind 0.0.0.0:8080 --workers 3 