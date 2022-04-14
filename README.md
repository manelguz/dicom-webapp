# dicom-webapp
A Django rest api based webapp to upload and visualize DICOM images

## To deploy de app to a webapp of azure

#az webapp up -g <group-name> -l westeurope -p <plan-name> --sku B1 -n <app-name> -r 'PYTHON:3.8'
#az webapp config appsettings set --settings AZURE_ACCOUNT_NAME=<account-name> AZURE_ACCOUNT_KEY=<account-key>