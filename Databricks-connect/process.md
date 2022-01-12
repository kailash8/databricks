# create python virtual environment

**--create command**
python -m venv deod-venv

**activate virtual env command**
--> In MacOS
source deod-venv/bin/activate
--> In WindowsOS
deod-venv\Scripts\activate
Below is reference:
C:\Users\choud\data-engineering-on-databricks>deod-venv\Scripts\activate

Note: Step 1 starts after enabling python virtual environment
## Set up the client
### Step 1: Install the client
**Uninstall PySpark. This is required because the databricks-connect package conflicts with PySpark. For details, see Conflicting PySpark installations.**

**Command**
pip uninstall pyspark

**Install the Databricks Connect client.**

**Command**
pip install -U "databricks-connect==9.1.*"  # or X.Y.* to match your cluster version.

### Step 2: Configure connection properties- Configure Databricks Connect

_**Following details are required:**_

databricks-connect-development
token: Generate token from azure databricks user settings
host: everything from https to databricks.com/net
cluster_id: text between cluster and configure

GO TO WINDOWS COMMAND LINE:

Run:
databricks-connect configure
After entering above command, we have to enter all required details.

Test connectivity to Databricks.
databricks-connect test


For more details: https://docs.databricks.com/dev-tools/databricks-connect.html
