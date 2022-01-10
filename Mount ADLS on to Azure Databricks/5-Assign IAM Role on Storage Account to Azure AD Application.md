## Assign IAM Role on Storage Account to Azure AD Application

**Steps:**
1. Search for Storage account in search bar of azure portal
2. Select desired storage account
3. Go to access control (IAM)
4. Click on Add and then 'Add role assignment'
5. Search for 'Storage Data Blob Contributor'
6. Click on next and then click on Next
7. Click on select members
8. Search for azure app registration which we had created earlier (ADLS-Databricks-Mount-Demo)
9. Click on select once azure app registration is selected
10. Click next and then review+assign


Below screenshot for referance :
![image](https://user-images.githubusercontent.com/48403668/148785419-70024cff-cf7f-4a63-ac2c-dec356c9f02c.png)


![image](https://user-images.githubusercontent.com/48403668/148785375-6a5cefa4-f173-4bda-8c94-6a603855dae4.png)


