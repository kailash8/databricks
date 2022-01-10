**For azure CLI help** \
az -h \
OR \
az group -h so on... \

**create resource group using Azure CLI** \
az group create \
-l eastus(available-location) \
-h testrgdemo(any-name-for-resource-group)

**To get list of each resource-group available on current logged in account** \
az group list query '[*].name()'

