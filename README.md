# Malavika S — Azure Data Engineering Project

End-to-end ETL pipeline built on Azure, using Azure Data Factory and Azure Databricks to ingest, transform, and process data through a Bronze → Silver → Gold medallion architecture.

![Azure](https://img.shields.io/badge/Azure-0078D4?style=flat&logo=microsoftazure&logoColor=white)
![Databricks](https://img.shields.io/badge/Databricks-FF3621?style=flat&logo=databricks&logoColor=white)
![PySpark](https://img.shields.io/badge/PySpark-E25A1C?style=flat&logo=apachespark&logoColor=white)
![Delta Lake](https://img.shields.io/badge/Delta%20Lake-00ADD8?style=flat)

---

## Overview

This project demonstrates a complete Azure data engineering workflow — from raw data ingestion to analytics-ready output — using industry-standard tools and the medallion (Bronze/Silver/Gold) architecture pattern.

## Architecture


[Source system:On-premise SQL DB]->ADL location->Azure Data Factory ──► Azure Data Lake Storage->Azure Databricks (PySpark + Delta -Lake)>Bronze(raw),Silver(cleaned),Gold(aggregated)
                                                                                                                               

## Tech stack

| Layer | Tools |
|---|---|
| Orchestration & Ingestion | Azure Data Factory |
| Storage | Azure Data Lake Storage Gen2 |
| Processing | Azure Databricks, PySpark, Delta Lake |
| Data format | Parquet / Delta |

## What this project does

- **Ingests** raw data from [source system] into Azure Data Lake Storage using Azure Data Factory pipelines.
- **Bronze layer** — lands raw data as-is with minimal transformation, preserving the original source structure.
- **Silver layer** — cleans and standardizes the data: handling nulls, correcting data types, removing duplicates.
- **Gold layer** — produces aggregated, analytics-ready tables suitable for reporting or downstream consumption.
- Built using PySpark notebooks in Databricks, with Delta Lake for reliable, versioned storage at each layer.

## Repository structure

MALAVIKA-S/
├── README.md
├── adf-pipelines/ # Exported ADF pipeline definitions
├── notebooks/
│ ├── bronze/
│ ├── silver/
│ └── gold/
└── docs/
└── screenshots/

## How to run this project

1. Clone the repo:
```bash
   git clone https://github.com/smalavika845-maker/MALAVIKA-S.git
```
2. Set up an Azure account with a Resource Group, ADLS Gen2 storage account, Azure Data Factory instance, and Azure Databricks workspace.
3. Import the pipeline JSON from `/adf-pipelines` into Data Factory.
4. Import the notebooks from `/notebooks` into Databricks and run them in order: Bronze → Silver → Gold.

## Future improvements

- Add automated data quality checks between layers
- Add Unity Catalog for governance and access control
- Set up CI/CD with GitHub Actions
- Add a Power BI dashboard on top of the Gold layer

## Author

**Malavika S**
Data Engineer | Azure · Databricks · PySpark · SQL
[LinkedIn](https://www.linkedin.com/in/malavika-s-35a383215) · smalavika845@gmail.com
