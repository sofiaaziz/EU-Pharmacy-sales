# 💊 Pharmacy Sales Exploratory Data Analysis & Dashboard


## 📖 About the Project
This project provides a comprehensive exploratory data analysis (EDA) of European pharmacy sales performance. By leveraging Python and Streamlit, this dashboard transforms raw transactional data into actionable insights regarding revenue trends, regional performance, and product category profitability.

Designed with a focus on **Supply Chain and Retail Analytics**, this dashboard helps identify:
*   High-performing products vs. low-margin items.
*   Regional sales variances and geographic distribution.
*   The impact of promotional activities on revenue.
*   Trends in generic vs. branded product adoption.

## 📊 Dashboard Structure
The application is organized into several interactive modules to allow for granular data exploration:

1.  **Home Page:** Introduction and high-level KPIs (Total Revenue, Units Sold, and Active Pharmacies).
2.  **📈 Sales Overview:** Visualizing temporal trends and the impact of promotions.
3.  **🌍 Regional Analysis:** Geographical breakdown of sales across countries and cities.
4.  **💊 Product Insights:** Deep-dive into category performance and brand distribution.
5.  **📊 Univariate Analysis:** Statistical distributions and frequency analysis of key financial metrics.
6.  **🔗 Multivariate Analysis:** Exploring correlations and relationships between revenue, costs, and margins.

## 📂 Data Dictionary
The analysis is based on the `Cleaned_Pharmacy_Sales.csv` dataset, which includes:

| Column | Description |
| :--- | :--- |
| **UnitsSold** | Quantity of items sold per transaction. |
| **RevenueEUR** | Total revenue generated from the sale in Euros. |
| **CostEUR** | Total cost of goods sold (COGS) in Euros. |
| **MarginEUR** | Profit margin calculated as (Revenue - Cost). |
| **PromoFlag** | Boolean indicator for promotional sales. |
| **Date** | Date of the transaction. |
| **PharmacyName** | Name of the specific pharmacy location. |
| **Country/Region/City** | Geographical hierarchy of the sales location. |
| **ProductName** | Name of the specific pharmaceutical product. |
| **Category** | High-level product classification (e.g., OTC, Wellness). |
| **IsGeneric** | Identifies if the product is a generic or branded item. |
| **ListPriceEUR** | The standard retail price of the item. |

## 🛠️ Tech Stack
*   **Language:** Python
*   **Framework:** Streamlit
*   **Data Analysis:** Pandas
*   **Visualization:** Plotly Express

## 🚀 How to Run Locally

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    cd your-repo-name
    ```

2.  **Install dependencies:**
    ```bash
    pip install streamlit pandas plotly
    ```

3.  **Run the application:**
    ```bash
    streamlit run main.py
    ```

---
*Developed by Sofia Aziz*