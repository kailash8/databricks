## Create Databricks Secret for AD Application Client Secret
**We need to first connect all the three dots of workflow.**
Three dots are as following.
1. ADLS Storage Account
2. AD(Active Directory) App Registration
3. Databricks Workspace

**_IN THIS FILE WE ARE FOCUSING ON 'How to Integrate the client secret value which is copied from previous file step with databricks CLI'_**

**Steps:**
1. On Azure Portal search for Azure Active directory
2. Create scope in cli or pthon virtual machine
3. Scope create command: databricks secrets create-scope --scope testadlsdbdemoscope --profile testadlsdb --initial-manage-principal "users" (uses mentioned to run command without error in case we don't have access of premium tier in azure databricks)
4. reference for step 3: ![image](https://user-images.githubusercontent.com/48403668/148780639-2ff408d7-01c5-4b60-adee-e96a865f772c.png)
5. Update scope with key and value
6. command for updating scope with key and value: databricks put --scope testadlsdbdemoscope --key testadlsdbdemokey --profile testadlsdb
7. Screenshot for the reference of 6th step as we can see it will open window to enter key. ![image](https://user-images.githubusercontent.com/48403668/148781276-b0d5ff79-fe28-4074-88a1-cf1aa04ddb19.png)
