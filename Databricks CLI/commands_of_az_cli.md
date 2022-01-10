**For azure CLI help** \
az -h \
OR \
az group -h so on... \

**create resource group using Azure CLI**  (Below command wont work in windows system but it will work in other CLIs. Make sure you write below command in single line in windows system) \
az group create \
-l eastus(available-location) \
-n testrgdemo(any-name-for-resource-group)

**To get list of each resource-group available on current logged in account** \
az group list query '[*].name()'

**get details of some specified resource-group** \
az group list --query "[?name=='testrgdemo']"

**Create Storage Account within Resource Group** \
az storage account \
-n testsademo (name-of-storage-account)\
-g testrgdemo (resource-group-for-which-this-storage-account-we-are-cerating)\
-l eastus (available-location) \
--sku standard_LRS (name-of-storage-plan)

**List all the Storage Accounts** \
az storage account list 

**Get List Storage Accounts associated with specified resource-group** \
az storage account list -g testrgdemo

**Delete specified storage account associated with some resource-group** \
az storage account delete -n testsademo -g testrgdemo
