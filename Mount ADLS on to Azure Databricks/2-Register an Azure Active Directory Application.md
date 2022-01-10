## Register an Azure Active Directory Application
**We need to first connect all the three dots of workflow.**
Three dots are as following.
1. ADLS Storage Account
2. AD(Active Directory) App Registration
3. Databricks Workspace

**_IN THIS FILE WE ARE FOCUSING ON 'ADLS Storage Account'_**

**Steps:**
1. On Azure Portal search for Azure Active directory
2. On left side options -> App Registrations -> New registration -> Enter name of AD like 'ADLS-Databricks-Mount-Demo' (Just an example name) 
3. Once AD created got to Certificates and secrets on left panel of newly cerated AD
4. Click on New Client Secret
5. Specify appropriate description like 'ADLS Databricks Mount Demo', click on add with default expiry period
6. Take backup of "value" once it is created. It will be client-secret-value.
7. Go to Overview
8. Copy Application (client) ID
9. Copy Directory (tenant) ID


Below screenshot for referance:

![image](https://user-images.githubusercontent.com/48403668/148768539-d2a6d695-8707-49f5-ab1e-f0c3fb61188b.png)
