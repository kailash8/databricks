## Mount ADLS Storage Account on to Azure Databricks
**Steps:**
1. Create a notebook in azure databricks
2. Set all the configurations regaring ADLS. Sample is given below where we need to replace required fields with real values. \ ![image](https://user-images.githubusercontent.com/48403668/149074459-a36c928d-5b16-4189-83e6-3096a4274a83.png)
3. Required values are replaced in below screenshot with all the values we fetched in previous sessions. ![image](https://user-images.githubusercontent.com/48403668/149074596-58937aaf-7da8-46cd-87d5-897f32497bec.png)
4. Set configurations of filesytem which is part of datastore on the databricks. Below screenshot showing all the fields to be fields with correct details.![image](https://user-images.githubusercontent.com/48403668/149074901-4291f4a5-90f8-4f8e-8630-a6696d39e9c0.png)
5. Required values are replaced with correct details. ![image](https://user-images.githubusercontent.com/48403668/149074993-adf93273-6da4-4aa4-a378-93fa66a5802d.png)
6. To verify : ![image](https://user-images.githubusercontent.com/48403668/149075122-fb58cfd1-6544-457a-ac28-502041a1e90e.png)


**Configs from step 3:** \
configs = {"fs.azure.account.auth.type": "OAuth", \
           "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider", \
           "fs.azure.account.oauth2.client.id": f"{client_id}", \
           "fs.azure.account.oauth2.client.secret": f"{client_secret}", \
           "fs.azure.account.oauth2.client.endpoint": f"https://login.microsoftonline.com/{tenant_id}/oauth2/token"} \
           
**Configs from step 5:** \  
def mount_adls(container_name): \
  dbutils.fs.mount( \
    source = f"abfss://{container_name}@{storage_account_name}.dfs.core.windows.net/", \
    mount_point = f"/mnt/{storage_account_name}/{container_name}", \
    extra_configs = configs)
