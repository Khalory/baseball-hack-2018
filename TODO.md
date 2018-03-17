### Fenwayizer, Fenway Parkifier, FenwayParkImprinter, BaseballImprinter

- [x] Python 3 env -- use python3, pip3
- [x] Install Storage API for Python (https://github.com/Azure/azure-storage-python) -- pip3 install azure-storage-blob
- [ ] Create Storage Account with CLI -- *orig* and *imprinted* containers created, read-only to public
- [ ] Get1 command line
- [ ] Put1 command line
- [ ] Store in github


## Create Storage Account with CLI

az storage account create \
    --location "East US" \
    --name "imprinter" \
    --resource-group "imprinter" \
    --sku "Standard_ZRS"

Key: qELnM/SC2Sx90GcLebvUCruxz/ibFlUpa4JP9pQSdXxURJPIeHHQfIBULswkO9XToZe4wH61OqhlLyen6+wSgA==

