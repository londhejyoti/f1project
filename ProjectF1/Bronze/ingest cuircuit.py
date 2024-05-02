# Databricks notebook source
print("Hello word")

# COMMAND ----------

Mount Azure Data Lake using Service Principal

Steps to follow

1. Get client id, tenant_id and client_secret from key vault

2. Set Spark Config with App/ Client Id, Directory/ Tenant Id & Secret

3. Call file system utlity mount to mount the storage

4. Explore other file system utlities related to mount (list all mounts, unmount)

# COMMAND ----------

configs = {"fs.azure.account.auth.type": "OAuth",
          "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
          "fs.azure.account.oauth2.client.id": "<application-id>",
          "fs.azure.account.oauth2.client.secret": dbutils.secrets.get(scope="<scope-name>",key="<service-credential-key-name>"),
          "fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/<directory-id>/oauth2/token"}
