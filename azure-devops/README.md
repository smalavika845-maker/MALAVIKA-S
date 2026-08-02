# Azure DevOps CI/CD

This folder contains the Azure DevOps YAML pipelines and supporting scripts used to automate the deployment of Azure Databricks notebooks across multiple environments.

## Overview

The CI/CD pipeline follows a multi-stage deployment approach. Whenever changes are pushed to the `main` branch, Azure DevOps automatically triggers the pipeline, authenticates with Azure, generates a temporary Databricks access token, and deploys the latest notebooks to the target Databricks workspace.

The deployment process is environment-specific and supports both **Development** and **Production** workspaces.

---

## Folder Structure

```
azure-devops/
│
├── cicd-pipeline.yml              # Main pipeline definition
├── templates/
│   └── deploy-notebooks.yml       # Reusable deployment template
└── scripts/
    └── Databrickstoken.ps1        # Generates temporary Databricks access token
```

---

## Components

### 1. `cicd-pipeline.yml`

This is the main Azure DevOps pipeline.

**Responsibilities**

- Automatically triggers on every push to the `main` branch.
- Loads Azure DevOps Variable Groups for environment-specific configuration.
- Deploys notebooks to both Development and Production environments.
- Invokes the reusable deployment template.

---

### 2. `deploy-notebooks.yml`

This reusable YAML template performs the notebook deployment.

**Deployment Steps**

- Checks out the latest repository.
- Authenticates with Azure using the configured Service Connection.
- Retrieves Azure Databricks workspace information.
- Generates a temporary Databricks Personal Access Token.
- Installs the Azure Databricks CI/CD PowerShell module.
- Uploads all notebooks from the repository to the Databricks workspace.

The notebooks are deployed to:

```
/live
```

inside the target Azure Databricks workspace.

---

### 3. `Databrickstoken.ps1`

This PowerShell script securely generates a temporary Databricks Personal Access Token (PAT) using Azure Active Directory authentication.

Instead of storing permanent tokens, the deployment pipeline creates a short-lived token during execution, improving security and eliminating manual token management.

---

## Deployment Workflow

```
Developer Pushes Code
          │
          ▼
Azure DevOps Pipeline Trigger
          │
          ▼
Azure CLI Authentication
          │
          ▼
Retrieve Databricks Workspace
          │
          ▼
Generate Temporary PAT
          │
          ▼
Install Databricks CI/CD Tools
          │
          ▼
Deploy Notebooks to DEV
          │
          ▼
Deploy Notebooks to PROD
```

---

## Features

- YAML-based CI/CD pipeline
- Multi-stage deployment (Development and Production)
- Reusable deployment templates
- Azure CLI integration
- Secure authentication using Azure AD
- Automatic Databricks notebook deployment
- Environment-specific configuration using Azure DevOps Variable Groups

---

## Prerequisites

Before running the pipeline, configure:

- Azure DevOps Service Connections
- Azure DevOps Variable Groups
- Azure Databricks Workspace
- Azure Resource Groups
- Azure CLI permissions
- Required PowerShell modules

---

## Technologies Used

- Azure DevOps
- Azure Pipelines (YAML)
- Azure CLI
- Azure Databricks
- PowerShell
- Azure Databricks CI/CD Tools
