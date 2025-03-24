
# Marketing Campaign Analysis - Technical Documentation

## Project Overview

This document provides a technical overview of the marketing campaign performance analysis project, detailing the data preparation steps, tools used, and key calculations.

## 1. Data Sources

* The client provided a dataset containing marketing campaign data.
* Due to client confidentiality, the original dataset is not included in this repository.
* Anonymized or sample data was used for the Python scripts.

## 2. Data Preparation

* Data types were verified and adjusted as needed.
* The data was prepared for analysis within Power BI's Power Query Editor and for Python's Pandas Library.

## 3. Tools and Technologies

* **Python (Pandas):** Used for data processing, metric calculations, and data transformation.
* **DAX (Data Analysis Expressions):** Used for creating calculated measures.

## 4. Metric Calculations

### 4.1. Python (Pandas)

The following metrics were calculated using Python and the Pandas library:

* **Click-Through Rate (CTR):**
    ```python
    df['CTR'] = (df['Clicks'] / df['Impressions']) * 100
    ```
* **Conversion Rate:**
    ```python
    df['Conversion_Rate'] = (df['Conversions'] / df['Clicks']) * 100
    ```
* **Cost Per Click (CPC):**
    ```python
    df['CPC'] = df['Total_Spend'] / df['Clicks']
    ```
* **Cost Per Acquisition (CPA):**
    ```python
    df['CPA'] = df['Total_Spend'] / df['Conversions']
    ```
* **Return on Ad Spend (ROAS):**
    ```python
    df['ROAS'] = df['Revenue_Generated'] / df['Total_Spend']
    ```

### 4.2. DAX Measures

The following measures were created using DAX:

* **Conversion Rate:**
    ```dax
    Conversion Rate = DIVIDE(SUM('YourTableName'[Conversions]), SUM('YourTableName'[Clicks]))
    ```
* **CPC:**
    ```dax
    CPC = DIVIDE(SUM('YourTableName'[Total_Spend]), SUM('YourTableName'[Clicks]))
    ```
* **CPA:**
    ```dax
    CPA = DIVIDE(SUM('YourTableName'[Total_Spend]), SUM('YourTableName'[Conversions]))
    ```
* **ROAS:**
    ```dax
    ROAS = DIVIDE(SUM('YourTableName'[Revenue_Generated]), SUM('YourTableName'[Total_Spend]))
    ```

## 5. Python Script Details

The `campaign_analysis.py` script performs the following tasks:

* Loads anonymized or sample data from a CSV file.
* Calculates key marketing metrics (CTR, Conversion Rate, CPC, CPA, ROAS).
* Exports the processed data to a new CSV file.

## 6. Dashboard Report Images

The `images/` folder contains screenshots of the Power BI dashboard reports, including:

* **Marketing Channels Comparison Analysis:** Comparing campaign performance across different channels.
* **Campaign Performance Analysis:** Visualizing overall campaign performance.
* **Time Based Analysis:** Displaying trends over time.
* **Marketing Campaign Dashboard:** Overview of key performance indicators.

## 7. Deliverables

* `scripts/campaign_analysis.py`: Python script for data processing (using anonymized data).
* `images/`: Folder containing dashboard report images.
* `documentation/documentation.md`: This technical documentation file.
