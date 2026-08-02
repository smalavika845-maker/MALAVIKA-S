Activity	    &                Purpose
---------                    ----------
Look for all tables-        Retrieves all tables from the NEW schema in SQL Server.

ForEachSchemaTable-         Iterates through each table returned by the Lookup activity.

Copy each table-            Dynamically copies each SQL Server table to ADLS Gen2 in Parquet format (Bronze layer).

BronzetoSilver-             Executes a Databricks notebook to clean, standardize, and transform Bronze data into the Silver layer.

SilvertoGold-               Executes a Databricks notebook to aggregate and prepare analytics-ready Gold tables for reporting.
