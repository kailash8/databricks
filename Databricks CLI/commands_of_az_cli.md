### **For azure CLI help** 
az -h \
OR \
az group -h so on... 

### **create resource group using Azure CLI**  (Below command wont work in windows system but it will work in other CLIs. Make sure you write below command in single line in windows system) (See this command in raw)
az group create \
-l eastus(available-location) \
-n testrgdemo(any-name-for-resource-group)

### **To get list of each resource-group available on current logged in account** 
az group list query '[*].name()'

### **get details of some specified resource-group** 
az group list --query "[?name=='testrgdemo']"

### **Create Storage Account within Resource Group** (See this command in raw) 
az storage account \
-n testsademo (name-of-storage-account)\
-g testrgdemo (resource-group-for-which-this-storage-account-we-are-cerating) \
-l eastus (available-location) \
--sku standard_LRS (name-of-storage-plan)

### **List all the Storage Accounts** 
az storage account list 

### Get List Storage Accounts associated with specified resource-group** 
az storage account list -g testrgdemo

### **Delete specified storage account associated with some resource-group** 
az storage account delete -n testsademo -g testrgdemo

### Add Containers as part of Storage Account (Create FileSystem or Conatiner for Storage Account)
az storage fs create -n data (this is name of fs or container) --account-name testadlsdemo

### List all the container and storage given inside specified storage account
az storage fs list --account-name testadlsdemo


## Current status
container name data within storage account \
itvazureclidemo -resource-group \
itvadlsdemo -storage-account \
data -filesystemORcontainer-name

### Upload the directory(local) into the Container or filesystem (Storage-account)
az storage fs directory upload -f data --account-name itvadlsdemo -s "local-path" --recursive

### validate if data got uploaded successfuly or not
az stoorage fs directory list -f data --account-name itvadlsdemo

### Get details of files in directory
az storage fs file list -f data --path(location-of-folder-in-container i.e. retail_db) --account-name itvadlsdemo

### Delete Storage Account
az storage account delete -n itvadlsdemo -g itvazureclidemo

### Delete Resource Group
az group delete -n itvazureclidemo

![image](https://user-images.githubusercontent.com/48403668/148754117-d53babc4-1389-4da9-a01b-a5ac01e778a2.png)
