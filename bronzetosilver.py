# Databricks notebook source
# DBTITLE 1,AUTH SETUP
spark.conf.set(
    "fs.azure.account.key.maludatalakegen2.dfs.core.windows.net",
    "FMUDsG0a+vNUE8zvYWXUaoyRiIUBONDhIeN0DouK3dM3nUZj+MBhyK/1mHH2rRecXjAbPm1yiLEm+AStlNZKJA=="
)

# COMMAND ----------

# DBTITLE 1,CONTAINER CHECK
display(dbutils.fs.ls("abfss://bronze@maludatalakegen2.dfs.core.windows.net/NEW"))

# COMMAND ----------

# DBTITLE 1,AGE BLOB CHECK
df1=spark.read.parquet('abfss://bronze@maludatalakegen2.dfs.core.windows.net/NEW/AGE')
df1.display()

# COMMAND ----------

# DBTITLE 1,SALARY BLOB CHECK
df2=spark.read.parquet('abfss://bronze@maludatalakegen2.dfs.core.windows.net/NEW/salary')
df2.display()

# COMMAND ----------

# DBTITLE 1,MARKS BLOB CHECK
df3=spark.read.parquet('abfss://bronze@maludatalakegen2.dfs.core.windows.net/NEW/Marks')
df3.display()

# COMMAND ----------

# MAGIC %md
# MAGIC DOING TRANSFORMATION FOR ALL TABLES

# COMMAND ----------

# DBTITLE 1,SPLITTING ON FOLDER BASIS
table_name=[]
for i in dbutils.fs.ls("abfss://bronze@maludatalakegen2.dfs.core.windows.net/NEW"):    

    table_name.append(i.name.split('/')[0])

# COMMAND ----------

# DBTITLE 1,TABLE NAME DISPLAY
table_name

# COMMAND ----------

# DBTITLE 1,MAIN TRANSFORMATION CODE SNIPPET
from pyspark.sql.functions import from_utc_timestamp,date_format
from pyspark.sql.types import TimestampType
for i in table_name:
    path='abfss://bronze@maludatalakegen2.dfs.core.windows.net/NEW/'+i+'/'+i+'.parquet'
    df=spark.read.format("parquet").load(path)
    column=df.columns
    for col in column:
        if "Date" in col or "date" in col:
            df=df.withColumn(col,date_format(from_utc_timestamp(df[col].cast(TimestampType()),'UTC'),"yyyy-MM-dd"))
    output_path='abfss://silver@maludatalakegen2.dfs.core.windows.net/NEW/'+i+'/'
    df.write.format('delta').mode('overwrite').save(output_path)     
        

# COMMAND ----------

# DBTITLE 1,CROSS-CHECK IN SILVER JUST FOR FUN
# df4=spark.read.format('delta').load('abfss://silver@maludatalakegen2.dfs.core.windows.net/NEW/salary')
# df4.display()