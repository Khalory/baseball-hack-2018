#/bin/bash

az login

az group create --name examplegroup --location "South Central US"
az group deployment create --resource-group examplegroup --template-file imprinter_storage_deploy.json

az storage account create \
    --location "East US" \
    --name "imprinter" \
    --resource-group "imprinter" \
    --sku "Standard_ZRS"
