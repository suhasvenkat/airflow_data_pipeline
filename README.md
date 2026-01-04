# Airflow Data Pipeline for Deep Learning–Based Energy Forecasting

This repository contains an **end-to-end data engineering and deep learning research pipeline** built using **Apache Airflow**, **Python**, **PostgreSQL**, and **Docker**.  
The project automates data ingestion, transformation, and storage, and supports **deep learning models for energy consumption forecasting** as part of an academic research study.

---

## 🚀 Project Overview

The goal of this project is to design a **reproducible and scalable pipeline** that connects **data engineering workflows** with **deep learning research**.

The system:
- Ingests raw CSV datasets automatically
- Cleans and transforms data consistently
- Stores structured data in PostgreSQL
- Feeds prepared datasets into deep learning models
- Enables reproducible experiments for time-series energy forecasting

This architecture reflects a real-world ML system where **Apache Airflow manages data orchestration** and **deep learning models handle prediction and analysis**.

---

## 🧰 Tech Stack

- **Apache Airflow (Astro Runtime)** – Workflow orchestration  
- **Python** – ETL and modeling logic  
- **Pandas & NumPy** – Data preprocessing  
- **PostgreSQL** – Structured data storage  
- **Docker & Docker Compose** – Containerized execution  
- **TensorFlow / Keras** – Deep learning models  
- **pgAdmin** – Database inspection  

---

## 📁 Project Structure

airflow_data_pipeline/
├── dags/
│ └── load_excel_to_postgres.py # Airflow DAG
├── include/
│ └── data/
│ ├── building_metadata.csv # Building metadata
│ └── weather.csv # Weather data
├── tests/
│ └── dags/ # DAG tests
├── Dockerfile
├── requirements.txt
├── packages.txt
├── airflow_settings.yaml
├── config.yaml
└── README.md


---

## 🔄 ETL Pipeline Workflow

### 1. Extract
- Reads raw CSV files from the `include/data/` directory

### 2. Transform
- Standardizes column names
- Handles missing and inconsistent values
- Removes duplicates
- Prepares features required for forecasting models

### 3. Load
- Stores transformed data into PostgreSQL tables:
  - `building`
  - `weather`

### 4. Orchestration
- The entire workflow is managed using an Apache Airflow DAG
- DAGs can be triggered manually or scheduled

---

## 🧠 Deep Learning & Research Component

The data processed through this pipeline is used for **deep learning–based energy forecasting research**.  
The pipeline ensures **consistent, reproducible, and scalable data preparation** across multiple experiments.

---

## 🤖 Deep Learning Models Implemented

### 🔹 LSTM (Long Short-Term Memory)
- Baseline model for time-series energy forecasting
- Captures temporal dependencies in building energy consumption
- Evaluated using MAE and error distributions

### 🔹 Transformer-Based Model
- Designed to capture long-range temporal relationships
- Compared against LSTM for accuracy and generalization
- Better performance on complex temporal patterns

### 🔹 Self-Supervised Pretraining (SSL)
- Models pretrained using self-supervised learning techniques
- Fine-tuned on labeled energy consumption data
- Improves robustness under:
  - Sparse data conditions
  - Noisy inputs
  - Simulated sensor failures

---

## 🔬 Research Questions Addressed

This project supports the following research questions:

- **RQ3:**  
  *What impact does self-supervised pretraining have on the robustness of deep energy forecasting models?*

- **RQ4:**  
  *Does integrating physical thermodynamic constraints into deep learning models improve forecast realism and generalization compared to purely data-driven approaches?*

---

## ⚙️ Role of Airflow in the Research

Apache Airflow is used to:
- Automate raw data ingestion
- Ensure consistent preprocessing across experiments
- Enable reproducible dataset generation
- Support scalable experimentation with multiple model variants

This separation mirrors real-world ML system design:
- **Airflow** → Data orchestration  
- **Deep Learning Models** → Prediction and evaluation  

---

## 📊 Model Outputs & Evaluation

The experiments produced:
- Training and validation loss curves
- Prediction vs actual energy consumption plots
- Error distribution and robustness analysis
- Performance comparison across clean, sparse, and failure scenarios

All figures used in the final research report were generated using data prepared by this pipeline.

---

## ▶️ How to Run the Project

### 1. Start Airflow
```bash
astro dev start
