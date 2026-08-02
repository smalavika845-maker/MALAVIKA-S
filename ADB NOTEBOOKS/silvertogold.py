# Databricks notebook source
# DBTITLE 1,Auth setup
spark.conf.set(
    "fs.azure.account.key.maludatalakegen2.dfs.core.windows.net",
    "FMUDsG0a+vNUE8zvYWXUaoyRiIUBONDhIeN0DouK3dM3nUZj+MBhyK/1mHH2rRecXjAbPm1yiLEm+AStlNZKJA=="
)

# COMMAND ----------

# DBTITLE 1,Mount path check
display(dbutils.fs.ls("abfss://silver@maludatalakegen2.dfs.core.windows.net/NEW"))

# COMMAND ----------

# DBTITLE 1,Age check
df1=spark.read.format('delta').load('abfss://silver@maludatalakegen2.dfs.core.windows.net/NEW/AGE')
df1.display()

# COMMAND ----------

# DBTITLE 1,Salary check
df2=spark.read.format('delta').load('abfss://silver@maludatalakegen2.dfs.core.windows.net/NEW/salary')
df2.display()

# COMMAND ----------

# DBTITLE 1,Marks check
df3=spark.read.format('delta').load('abfss://silver@maludatalakegen2.dfs.core.windows.net/NEW/Marks')
df3.display()

# COMMAND ----------

# DBTITLE 1,SPLIT FOLDERS
table_name=[]
for i in dbutils.fs.ls("abfss://silver@maludatalakegen2.dfs.core.windows.net/NEW"):    

    table_name.append(i.name.split('/')[0])

# COMMAND ----------

table_name

# COMMAND ----------

# DBTITLE 1,MAIN TRANSFORMATION
for name in table_name:
    df = spark.read.format("delta").load('abfss://silver@maludatalakegen2.dfs.core.windows.net/NEW/' + name)

    # Get the list of column names
    column_names = df.columns

    for old_col_name in column_names:
        # Convert column name from CamelCase to Column_Name Format
        new_col_name = "".join(["_" + char if char.isupper() and (i > 0 and not old_col_name[i-1].isupper()) else char for i, char in enumerate(old_col_name)]).lstrip("_")
        
        # Only rename if the new name is different and does not already exist
        if new_col_name != old_col_name and new_col_name not in column_names:
            df = df.withColumnRenamed(old_col_name, new_col_name)

    output_path = f'abfss://gold@maludatalakegen2.dfs.core.windows.net/NEW/{name}/'
    df.write.format("delta").mode("overwrite").save(output_path)

# COMMAND ----------

# DBTITLE 1,CROSS-CHECK
df4=spark.read.format('delta').load('abfss://gold@maludatalakegen2.dfs.core.windows.net/NEW/Marks')
df4.display()