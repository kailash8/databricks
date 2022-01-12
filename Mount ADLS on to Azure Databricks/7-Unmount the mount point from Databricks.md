# Unmount the mount point from Databricks

**Process**

Just run below mentioned piece of code in notebook. 
--> dbutils.fs.unmount("<PathOfMountPoint i.e. /mnt/data>")

Below screenshot for referance :
![image](https://user-images.githubusercontent.com/48403668/149090997-b2913289-5319-4088-bfde-9d98c47c7ef9.png)

This cleanup is required so that we are not charged un-neccesary. 
After Unmounting mount point we can delete resource group and storage accounts.
