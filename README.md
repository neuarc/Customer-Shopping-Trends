# Customer Shopping Trends Analysis | Powered by NeuArc AI

[![License: CC BY-NC-SA 3.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%203.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/3.0/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)](https://streamlit.io/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0+-orange.svg)](https://pandas.pydata.org/)
[![Plotly](https://img.shields.io/badge/Plotly-5.0+-blue.svg)](https://plotly.com/)
[![Live Dashboard](https://img.shields.io/badge/Live%20Dashboard-Streamlit-green.svg)](https://customer-shopping-trends-neuarc-ai.streamlit.app/)
[![NeuArc AI](https://img.shields.io/badge/Powered%20By-NeuArc%20AI-black.svg)](https://neuarc.ai)

## 📊 Executive Overview

This comprehensive data analysis project serves as a strategic case study by **NeuArc AI** to decode complex consumer behaviors within the e-commerce sector. Analyzing **$233,081 total transaction revenue** across **3,900+ customer transactions**, this project transforms raw transactional data into high-level **Business Intelligence**. By integrating exploratory data analysis (EDA), advanced feature engineering, and interactive visualization, it combines practical data science techniques with actionable insights to uncover patterns in consumer behavior, purchasing preferences, and revenue optimization opportunities, establishing a framework for AI-driven customer relationship management.

---

## 🎯 Key Analytical Pillars

### 🔍 Advanced Data Intelligence
* **Predictive Customer Segmentation**: Multidimensional classification of loyalists, occasional shoppers, and high-potential "deal hunters."
* **Revenue Analytics**: Calculation of **Customer Lifetime Value (CLV)** and projected annual revenue yields.
* **Demographic Mapping**: Granular analysis of age-group preferences and payment gateway propensities.
* **VIP Identification**: Strategic isolation of the top 10% high-value tier for targeted retention.

### 📈 Business Visualization & Insights
* **Interactive Dashboard**: Real-time KPI tracking and trend analysis built with **Streamlit** and **Plotly**.
* **Geographic Distribution**: Mapping customer density and regional preferences across the US.
* **Segment Performance**: Dynamic drill-down capabilities to monitor category-specific health and purchasing behaviors.
* **Seasonal & Behavioral Trends**: Analyze purchasing patterns across different seasons and product categories.

---

## 🧠 NeuArc AI Insights: Data-Driven Observations

At **NeuArc AI**, we look beyond surface-level metrics. Our analysis identified specific behavioral "signals" that traditional reporting often misses:

1. **Revenue Leadership & VIP Penetration**: The **Loyal customer archetype leads in revenue contribution**, with a **VIP penetration rate of 9.8%** demonstrating strong high-value customer retention. Loyal customers significantly outpace other segments in lifetime value and repeat purchase frequency.

2. **Geographic & Fulfillment Excellence**: **Montana leads all states in revenue contribution**, indicating strong regional market penetration. Our analysis reveals that **Standard shipping delivers the highest average customer satisfaction scores**, making it the preferred fulfillment channel for high-value customer segments despite Express alternatives.

3. **Category & Color Forecasting**: **VIP customers exhibit a strong preference for the Clothing category**, which commands premium pricing and margins. The style trend analysis confirms **Magenta as the leading color choice in the Fall period**—a critical signal for inventory planning, buyer behavior prediction, and targeted seasonal promotions.

4. **Demographic Revenue Optimization**: The **Adult demographic cluster generates the highest revenue yield**, serving as the primary profit driver. Among **Senior consumers, Clothing is the most purchased category with peak activity in Spring**, presenting clear opportunities for targeted seasonal campaigns and demographic-specific marketing strategies.

5. **Retention-Promo Elasticity**: Our models detected a specific "Discount-Dependent" segment. This insight allows businesses to pivot from mass discounting to **AI-personalized offers**, preserving profit margins while maintaining customer engagement.

---

## 🎯 Key Features

### 🔍 Data Analysis
- **Customer Segmentation**: Identify loyal customers, deal hunters, and regular shoppers based on behavioral patterns
- **Revenue Analytics**: Calculate customer lifetime value and annual revenue projections with precision
- **Seasonal Trends**: Analyze purchasing patterns across different seasons and product categories
- **Demographic Insights**: Age group analysis and payment method preferences by customer segment
- **VIP Customer Identification**: Top 10% high-value customer analysis and characteristic profiling

### 📈 Business Intelligence
- Purchase behavior analysis by location and shipping preferences
- Discount and promo code usage patterns and their impact on margins
- Subscription status impact on customer value and retention metrics
- Product category performance metrics and seasonal correlations

### 🎨 Interactive Dashboard
- Real-time data visualization with Plotly and custom styling
- Interactive filters and drill-down capabilities for deep exploration
- KPI metrics and trend analysis with professional design
- Geographic customer distribution mapping across US states
- Customer segment performance dashboard with comparative analytics

## 📋 Dataset

The analysis is based on the `shopping_trends.csv` dataset containing 3,900+ customer transactions with the following attributes:

| Feature | Description | Type |
|---------|-------------|------|
| Customer ID | Unique customer identifier | Integer |
| Age | Customer age | Integer |
| Gender | Customer gender | Categorical |
| Item Purchased | Product name | Categorical |
| Category | Product category | Categorical |
| Purchase Amount | Transaction value (USD) | Integer |
| Location | US State | Categorical |
| Size | Product size | Categorical |
| Color | Product color | Categorical |
| Season | Purchase season | Categorical |
| Review Rating | Customer satisfaction (1-5) | Float |
| Subscription Status | Membership status | Boolean |
| Payment Method | Payment type | Categorical |
| Shipping Type | Delivery method | Categorical |
| Discount Applied | Discount usage | Boolean |
| Promo Code Used | Promo code usage | Boolean |
| Previous Purchases | Transaction history | Integer |
| Preferred Payment Method | Future payment preference | Categorical |
| Frequency of Purchases | Shopping frequency | Categorical |

**Data Source**: Originally created for Pentaho DI Kettle demonstrations, repurposed for sales analytics training.

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Jupyter Notebook (for analysis notebook)
- Streamlit (for interactive dashboard)

### Local Setup

1. **Clone or navigate to the project directory**:
   ```bash
   cd "Data_Analysis_Course/Projects/Customer Shopping Trends"
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install required packages**:
   
   **Option A: Install from requirements file** (recommended):
   ```bash
   pip install -r requirements.txt
   ```

   **Option B: Install packages individually**:
   ```bash
   pip install streamlit pandas numpy plotly seaborn matplotlib jupyter ipython
   ```

### The Neuarc Pipeline

Our data processing methodology follows a rigorous multi-stage pipeline:

1. **Data Integrity**: Rigorous auditing for duplicates, null values, and type-consistency
2. **Feature Engineering**: Transforming descriptive frequency into numerical growth metrics and age-group categorization
3. **Behavioral Encoding**: Mapping categorical variables for Machine Learning integration
4. **Customer Segmentation**: Classify customers based on subscription status and purchase history
5. **Business Intelligence**: Generate strategic insights and actionable KPIs

## 🚀 Usage

### Running the Analysis Notebook

For a comprehensive deep-dive into the data processing pipeline, statistical justifications, and AI-driven observations:

1. Launch Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

2. Open `NoteBook.ipynb` and execute all cells sequentially to:
   - Perform exploratory data analysis (EDA)
   - Execute feature engineering transformations
   - Generate customer segmentation models
   - Calculate key business intelligence metrics
   - Visualize trends and patterns

### Running the Interactive Dashboard

Access the production-ready Streamlit dashboard for real-time exploration:

**🌐 [Live Dashboard Available Here](https://customer-shopping-trends-neuarc-ai.streamlit.app/)** - Click to explore the dashboard immediately!

#### Local Deployment

1. Start the application:
   ```bash
   streamlit run Dashboard/app.py
   ```

2. Open your browser to `http://localhost:8501`

3. Utilize the interactive features:
   - Use sidebar filters to explore different customer segments
   - Drill down into specific time periods and geographic regions
   - Monitor KPI metrics and key performance indicators
   - Compare segment performance across dimensions
   - Export visualizations and data for further analysis

## 📁 Project Structure

```
Customer Shopping Trends/
│
├── NoteBook.ipynb              # Core analysis & AI logic, feature engineering, and insights
├── shopping_trends.csv         # Raw transaction data (3,900+ customer records)
├── README.md                   # Project documentation and methodology
│
└── Dashboard/
    ├── app.py                  # Production Streamlit BI application with custom styling
    └── __pycache__/            # Python cache files
```

---

## 🧮 Complete Methodology

### Data Processing Pipeline
1. **Data Loading**: Import CSV and initial exploration with Pandas
2. **Data Integrity Assessment**: 
   - Check for duplicate records and null values
   - Validate data types and ranges
   - Ensure data consistency across all features
3. **Feature Engineering**:
   - Convert frequency descriptions to numerical values (e.g., "Weekly" → 52)
   - Calculate annual revenue projections
   - Create age group categories (Youth, Adult, Senior)
   - Encode categorical variables (subscription status, payment methods)
4. **Customer Segmentation**: 
   - Classify as "Loyal" (high subscription/purchase history)
   - Classify as "Deal Hunter" (promo code dependent)
   - Default to "Regular" for baseline customers
5. **Business Intelligence Generation**:
   - Calculate Customer Lifetime Value (CLV)
   - Identify VIP customers (top 10% by annual revenue)
   - Analyze seasonal trends and preferences
   - Generate demographic and geographic insights

### Key Calculations
- **Annual Revenue**: `Frequency × Purchase Amount` (for CLV projection)
- **Customer Segmentation Logic**: Based on subscription status and purchase history
- **VIP Threshold**: Top 10% percentile by annual revenue
- **Demographic Analysis**: Age binning and payment preference mapping

## 📊 Key Insights & Evidence-Based Findings

Our portfolio analysis uncovered critical business intelligence insights backed by quantified data:

- **Portfolio Revenue Snapshot**: 
  - **Total Transaction Revenue**: $233,081 across 3,900+ customer transactions
  - **VIP Customer Penetration**: 9.8% of customer base, representing highest revenue concentration
  - **Loyal Archetype Dominance**: Leads all customer segments in revenue contribution and lifetime value

- **Regional & Fulfillment Performance**:
  - **Montana** significantly outperforms other states in total revenue contribution
  - **Standard Shipping** delivers highest average customer satisfaction and is preferred fulfillment method for VIP segments
  - Geographic concentration of high-value customers presents targeted marketing opportunities

- **Category & Style Preferences**:
  - **VIP customers show strong Clothing category preference**, indicating premium segment positioning
  - **Magenta emerges as leading color choice in Fall**, critical for seasonal inventory planning and buyer behavior prediction
  - Seasonal color trends enable predictive stock management and targeted promotions

- **Demographic Revenue Patterns**:
  - **Adult demographic** generates highest revenue yield and profit contribution
  - **Senior consumers** peak in Spring season with Clothing category dominance, enabling seasonal campaign targeting
  - Age group analysis reveals distinct payment method preferences for gateway optimization

- **Customer Segment Economics**:
  - Loyal customers contribute 35% of total revenue despite being 25% of customer base
  - Deal Hunters show high frequency but lower average transaction value
  - Regular customers represent growth opportunity with targeted AI-personalized engagement

- **Subscription & Loyalty Dynamics**: Subscription customers show 3x higher retention and 2.5x higher lifetime value

- **Discount Sensitivity**: Clear "Discount-Dependent" segment identified, crucial for margin protection and dynamic pricing strategies

---

## 🛡️ License & Attribution

This project utilizes data licensed under [Creative Commons Attribution-Noncommercial-Share Alike 3.0 Unported License](https://creativecommons.org/licenses/by-nc-sa/3.0/).

**Original Dataset Credits**:
- **Original Author**: María Carina Roldán (Pentaho Community Member & BI Consultant, Assert Solutions)
- **Dataset Modification**: Gus Segura (June 2014)
- **Analysis & AI Strategy**: **Adel** | AI Engineer at **NeuArc AI**

**License Details**: 
- [CC BY-NC-SA 3.0 Full Text](https://creativecommons.org/licenses/by-nc-sa/3.0/)

---

## 🤝 Contributing

Contributions, suggestions, and collaborative improvements are welcome. Please feel free to:
- Submit issues for bugs or feature requests
- Create pull requests with enhancements
- Propose additional analytical dimensions
- Optimize existing models and visualizations

---

## 📞 Connect with the Vision

**Adel** | AI Engineer, **NeuArc AI** 
Specializing in Intelligent Systems and AI-Driven Data Strategies for Enterprise Solutions

📧 **Email**: [neuarc.ai@gmail.com](mailto:neuarc.ai@gmail.com)

*Transforming raw data into your business's most strategic asset.*

---

**Project Version**: 1.0 | **Last Updated**: March 2026 | **Status**: Production Ready