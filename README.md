# End-To-End Azure Data Engineering Project Demonstrating ETL

End-to-end ETL pipeline built on Azure, using Azure Data Factory and Azure Databricks to ingest, transform, and process data through a Bronze → Silver → Gold medallion architecture.

![Azure](https://img.shields.io/badge/Azure-0078D4?style=flat&logo=microsoftazure&logoColor=white)
![Databricks](https://img.shields.io/badge/Databricks-FF3621?style=flat&logo=databricks&logoColor=white)
![PySpark](https://img.shields.io/badge/PySpark-E25A1C?style=flat&logo=apachespark&logoColor=white)
![Delta Lake](https://img.shields.io/badge/Delta%20Lake-00ADD8?style=flat)
![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=flat&logo=powerbi&logoColor=black)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-2088FF?style=flat&logo=githubactions&logoColor=white)

---

## Overview

This project demonstrates a complete Azure data engineering workflow — from raw data ingestion to analytics-ready output — using industry-standard tools and the medallion (Bronze/Silver/Gold) architecture pattern.

## Architecture


[Source system:On-premise SQL DB]->ADL location->Azure Data Factory ──► Azure Data Lake Storage->Azure Databricks (PySpark + Delta -Lake)->Bronze(raw),Silver(cleaned),Gold(aggregated)->Power BI dashboard-> CI/CD: GitHub Actions automates pipeline/notebook deployment
                                                                                                                               

## Tech stack

| Layer | Tools |
|---|---|
| Orchestration & Ingestion | Azure Data Factory |
| Storage | Azure Data Lake Storage Gen2 |
| Processing | Azure Databricks, PySpark, Delta Lake |
| Data format | Parquet / Delta |
| Reporting | Power BI |
| CI/CD | GitHub Actions |

## What this project does

- **Ingests** raw data from [source system] into Azure Data Lake Storage using Azure Data Factory pipelines.
- **Bronze layer** — lands raw data as-is with minimal transformation, preserving the original source structure.
- **Silver layer** — cleans and standardizes the data: handling nulls, correcting data types, removing duplicates.
- **Gold layer** — produces aggregated, analytics-ready tables suitable for reporting or downstream consumption.
- Built using PySpark notebooks in Databricks, with Delta Lake for reliable, versioned storage at each layer.
- **Power BI** — connects to the Gold layer to visualize key metrics and trends on an interactive dashboard.
- **CI/CD** — GitHub Actions automates deployment of pipeline and notebook changes, reducing manual release effort.

## Repository structure

MALAVIKA-S/
├── README.md
├── adf-pipelines/ # Exported ADF pipeline definitions
├── notebooks/
│ ├── bronze/
│ ├── silver/
│ └── gold/
├── .github/
│ └── workflows/ # CI/CD pipeline definitions
├── powerbi/
│ └── dashboard.pbix
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
5. Open `powerbi/dashboard.pbix` in Power BI Desktop and connect it to your Gold layer tables.
6. CI/CD workflows in `.github/workflows` run automatically on push to validate and deploy changes.

## Future improvements

- Add automated data quality checks between layers
- Add Unity Catalog for governance and access control
- Add real-time/streaming ingestion

## Author

**Malavika S** |
Data Engineer | Azure · Databricks · PySpark · SQL
[LinkedIn](https://www.linkedin.com/in/malavika-s-35a383215) · smalavika845@gmail.com
