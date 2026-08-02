# Power BI Dashboard

This folder contains the Power BI dashboard developed for the Azure Data Engineering ETL project.

The dashboard connects to the **Gold Layer** of the Medallion Architecture, where the transformed and business-ready data is stored as Delta/Parquet tables.

---

## Overview

The Power BI dashboard provides an interactive visualization of the processed data, enabling users to analyze business metrics and gain insights from the Gold layer.

The dashboard is built on top of the ETL pipeline, ensuring that only cleansed, validated, and aggregated data is used for reporting.

---

## Data Flow

```
SQL Server
     │
     ▼
Azure Data Factory
     │
     ▼
Azure Data Lake Storage Gen2
     │
     ▼
Azure Databricks
(Bronze → Silver → Gold)
     │
     ▼
Power BI Dashboard
```

---

## Dashboard Features

- Interactive reports and visualizations
- Business-ready KPIs
- Dynamic filtering and slicing
- Aggregated metrics from the Gold layer
- Clean and standardized reporting data

---

## Data Source

The dashboard is connected to the **Gold Layer**, which contains:

- Cleansed data
- Standardized schemas
- Aggregated business metrics
- Analytics-ready datasets

---


## Technologies Used

- Microsoft Power BI
- Azure Data Lake Storage Gen2
- Azure Databricks
- Delta Lake
- SQL

---

## Future Enhancements

- Real-time dashboard using streaming data
- Incremental refresh
- Row-Level Security (RLS)
- Scheduled dataset refresh
- Additional KPI visualizations
