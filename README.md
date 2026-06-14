# Data Storytelling & Statistical Validation Project

## Project Overview

This project represents the final stage of a complete Data Analytics workflow, covering Data Wrangling, Exploratory Data Analysis (EDA), Business Intelligence Dashboarding, Data Storytelling, and Statistical Validation.

The objective was to transform raw sales data into actionable business insights and present findings in a business-friendly format supported by statistical evidence.

---

## Business Objective

The company wanted to understand:

* Which products generate the highest revenue?
* Which customer segments contribute most to sales?
* Which cities drive business growth?
* What factors influence overall sales performance?
* How can data-driven insights support strategic decisions?

---

## Dataset Summary

* Dataset Type: Sales Transactions
* Records: 1000
* Features: Customer Information, Product Details, Sales Metrics, Demographics
* Data Preparation: Cleaning, Transformation, and Feature Engineering completed

---

## Project Workflow

### 1. Data Wrangling

* Data cleaning and preprocessing
* Missing value handling
* Duplicate removal
* Data type corrections
* Feature engineering

### 2. Exploratory Data Analysis

* Descriptive statistics
* Revenue analysis
* Customer demographics analysis
* Product category performance
* Correlation analysis

### 3. Business Intelligence Dashboard

* Interactive Power BI dashboard
* KPI tracking
* Dynamic filtering
* Customer segmentation visualization

### 4. Data Storytelling

* Business-focused narrative creation
* Insight communication
* Recommendation generation

### 5. Statistical Validation

* Hypothesis formulation
* Independent Two-Sample T-Test
* Business conclusion based on p-value interpretation

---

## Key Performance Indicators (KPIs)

### Total Revenue

Formula:

Total Revenue = SUM(Total_Sales)

Purpose:
Measures overall business performance and revenue generation.

---

### Total Orders

Formula:

Total Orders = COUNT(Order_ID)

Purpose:
Measures transaction volume and customer activity.

---

### Average Order Value (AOV)

Formula:

Average Order Value = Total Revenue / Total Orders

Purpose:
Evaluates average customer spending per order.

---

### Average Customer Age

Formula:

Average Customer Age = AVG(Age)

Purpose:
Provides demographic insights about customers.

---

## Deep-Dive Analysis: Customer Segmentation

### Objective

Identify customer groups based on purchasing behavior and revenue contribution.

### Segments

* Low Value Customers
* Medium Value Customers
* High Value Customers

### Findings

* High-value customers contribute a significant portion of total revenue.
* A small customer segment drives a large share of business performance.
* Customer segmentation enables targeted marketing and retention strategies.

---

## Statistical Hypothesis Testing

### Business Question

Do Male and Female customers differ significantly in their average purchase amount?

### Null Hypothesis (H₀)

There is no significant difference between Male and Female average purchase amounts.

### Alternative Hypothesis (H₁)

There is a significant difference between Male and Female average purchase amounts.

### Statistical Test Used

Independent Two-Sample T-Test

### Significance Level

α = 0.05

### Business Interpretation

The p-value obtained from the test was compared with the significance level to determine whether observed differences were statistically significant.

This helps validate business decisions using data rather than assumptions.

---

## Key Insights

### Customer Insights

* High-value customers generate the majority of revenue.
* Customer spending patterns vary across segments.

### Product Insights

* Certain categories consistently outperform others.
* Revenue is concentrated among top-performing products.

### Geographic Insights

* A few cities contribute most of the revenue.
* Regional sales patterns provide opportunities for targeted marketing.

### Business Performance Insights

* Revenue trends reveal potential seasonality.
* KPI monitoring supports strategic planning.

---

## Dashboard Features

### KPI Cards

* Total Revenue
* Total Orders
* Average Order Value
* Average Customer Age

### Interactive Visualizations

* Monthly Revenue Trend
* Revenue by Category
* Revenue by City
* Gender Distribution
* Customer Segmentation

### Filters

* City
* Gender
* Category
* Month

---

## Tools & Technologies

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* SQL
* Power BI
* Excel
* GitHub

---

## Project Structure

Data_Storytelling_Statistical_Validation

├── Dataset
│   └── Cleaned_Sales_Dataset.csv

├── Scripts
│   ├── data_cleaning.py
│   ├── eda_analysis.py
│   ├── customer_segmentation.py
│   └── hypothesis_testing.py

├── Dashboard
│   └── PowerBI_Dashboard.pbix

├── Presentation
│   └── Final_Presentation.pptx

├── Reports
│   ├── Deep_Dive_Report.pdf
│   └── Hypothesis_Testing_Summary.pdf

├── Screenshots
│   └── Dashboard_Images

└── README.md

---

## Business Recommendations

1. Focus retention efforts on high-value customers.
2. Introduce customer loyalty programs.
3. Increase marketing investment in high-performing cities.
4. Promote top-performing product categories.
5. Use dashboard insights for strategic decision-making.

---

## Conclusion

This project demonstrates the complete data analytics lifecycle—from raw data preparation to business storytelling and statistical validation. By combining analytics, visualization, and hypothesis testing, meaningful insights were generated to support data-driven business decisions.
