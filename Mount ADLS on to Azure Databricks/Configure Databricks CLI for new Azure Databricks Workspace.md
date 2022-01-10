## Configure Databricks CLI for new Azure Databricks Workspace

**Steps:**
1. Create token from user setting of azure databricks workspace
2. Copy host from link (link of azure databricks workspace till .net)
3. Copy token and use it next steps
4. Install databricks-cli (wherever you want, can be python Virtual Environment or any other CLI)
5. Try given command. --> databricks configure --token --profile demoprofile (any name just avoid changes in default profile)
6. Prompt will be generated for host and token. Enter write details.
7. Check it was successful attempt or not. command: databricks fs ls --profile demoprofile
8. databricks-results directory should get generated if it is successful.


Below screenshot for referance (Below screenshots of Python Virtual Environment):
![image](https://user-images.githubusercontent.com/48403668/148761924-91a1aba3-cfa8-482e-9eec-60e112fa7470.png)
![image](https://user-images.githubusercontent.com/48403668/148761969-d8408fe9-0a9a-499e-a83e-a3fdd28160ae.png)
