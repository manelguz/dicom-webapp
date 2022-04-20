# dicom-webapp
A Django rest api based webapp to upload and visualize DICOM images

# Test


coverage run --source='.' manage.py test
coverage report

# Docker
docker build --build-arg azure_name=<> --build-arg azure_key=<>  --build-arg django_key=<>  . -t dicomapp
docker run -it -p 8080 dicomapp

## To deploy de app to a webapp of azure

az webapp up -g <group-name> -l westeurope -p <plan-name> -r 'PYTHON:3.8'
az webapp config appsettings set --settings AZURE_ACCOUNT_NAME=<account-name> AZURE_ACCOUNT_KEY=<account-key> SECRET_KEY=<djanngo-secret-key>