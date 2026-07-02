# 📊 GA4 E-commerce Product Analytics

> **End-to-end Product Analytics Project** using **Google Analytics 4, BigQuery, dbt, Python, Machine Learning, Tableau, and Streamlit**.

This project investigates one core business question:

> **Why do users abandon the checkout process, and how can we identify high-intent users before they leave?**

Starting from raw Google Analytics 4 (GA4) event data, this project builds an end-to-end analytics pipeline covering data engineering, product analytics, machine learning, interactive dashboards, and cloud deployment.

---

# 🚀 Live Demo

| Resource | Link |
|----------|------|
| 🌐 Streamlit App | https://ga4-product-analytics-331058043654.europe-west9.run.app |
| 📈 Tableau Dashboard | https://public.tableau.com/views/Book1_17830071008490/GA4E-commerceProductAnalytics?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link |
| 🎥 Project Presentation | *Coming Soon* |

---

# 📌 Business Problem

Although thousands of users browse products, only a small percentage complete a purchase.

This project aims to answer the following business questions:

- Where do users leave the purchase journey?
- Which stages cause the largest conversion loss?
- Which customer segments convert better?
- Can purchase intent be predicted before users leave?
- How can these insights support product optimization?

---

# 🛠 Tech Stack

| Category | Technologies |
|-----------|--------------|
| Data Warehouse | Google BigQuery |
| Data Modeling | dbt |
| Programming | Python |
| Data Analysis | Pandas, NumPy |
| Machine Learning | Scikit-learn, Random Forest, XGBoost |
| Visualization | Plotly, Tableau |
| Dashboard | Streamlit |
| Deployment | Docker, Google Cloud Run |

---

# 📂 Project Structure

```text
.
├── app/                    # Streamlit application
│   ├── Home.py
│   ├── pages/
│   │   ├── 01_Funnel.py
│   │   ├── 02_Checkout.py
│   │   └── 03_Prediction.py
│   └── assets/
│
├── dbt/                    # Data transformation project
│   ├── models/
│   │   ├── staging/
│   │   ├── intermediate/
│   │   └── marts/
│
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_product_analysis.ipynb
│   └── 03_purchase_intent_prediction.ipynb
│
├── models/                 # Trained ML models
├── outputs/                # Model comparison & feature importance
├── src/                    # BigQuery services & SQL queries
├── tableau/                # Tableau workbook
└── Dockerfile
```

---

# 🔄 Project Workflow

```text
GA4 Raw Events
        │
        ▼
Google BigQuery
        │
        ▼
dbt Modeling
(Staging → Intermediate → Mart)
        │
        ▼
Exploratory Data Analysis
        │
        ▼
Business Analysis
        │
        ▼
Machine Learning
(Random Forest)
        │
        ▼
Tableau Dashboard
        │
        ▼
Streamlit Application
        │
        ▼
Google Cloud Run
```

---

# 📖 Project Components

## 1️⃣ Data Engineering

Raw Google Analytics 4 event data is transformed using **dbt** into reusable analytical models.

### Staging

- Clean raw GA4 events
- Extract nested event parameters
- Standardize schema

### Intermediate

Build session-level datasets including:

- Session duration
- User engagement
- Product interactions
- Acquisition channels
- Device information

### Mart Tables

Business-ready datasets include:

- `mart_funnel`
- `mart_checkout_abandonment`
- `mart_purchase_prediction`
- `mart_kpi_summary`

---

## 2️⃣ Exploratory Data Analysis

Notebook:

```
01_data_understanding.ipynb
```

Topics covered:

- Dataset overview
- Missing values
- Event distribution
- User behavior
- Device distribution
- Traffic source analysis
- Country analysis

---

## 3️⃣ Product Analytics

Notebook:

```
02_product_analysis.ipynb
```

Business analyses include:

- Purchase Funnel
- Checkout Abandonment
- Product Engagement
- User Segmentation
- Device Performance
- Traffic Source Analysis

### Key Insight

The largest conversion loss occurs between **View Item** and **Add to Cart**, indicating friction before users enter the checkout process.

---

## 4️⃣ Purchase Intent Prediction

Notebook:

```
03_purchase_intent_prediction.ipynb
```

Models evaluated:

- Logistic Regression
- Random Forest
- Tuned Random Forest
- XGBoost

Feature engineering:

- Engagement per event
- Item view rate
- Checkout ratio

Evaluation metrics:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC

The best-performing model (**Tuned Random Forest**) is deployed in the Streamlit application for interactive purchase prediction.

---

# 📊 Interactive Dashboards

## 🏠 Home

Executive dashboard providing:

- Dataset overview
- KPI summary
- Funnel overview
- Device distribution
- Country distribution
- Traffic source distribution

---

## 📈 Funnel Analysis

Visualize user conversion throughout the purchase journey.

Features:

- Funnel visualization
- Stage conversion
- Drop-off analysis
- Business recommendations

---

## 🛒 Checkout Analysis

Analyze checkout abandonment.

Features:

- Checkout KPIs
- Checkout funnel
- Abandoned vs completed sessions
- Device comparison
- Country comparison
- Traffic source comparison

---

## 🤖 Purchase Intent Prediction

Interactive machine learning dashboard.

Features:

- Model comparison
- Feature importance
- High-intent user distribution
- Purchase probability prediction
- Business action recommendations

---

# 📈 Tableau Dashboard

Interactive executive dashboard built with Tableau Public.

Includes:

- Executive KPIs
- Purchase Funnel
- Device Analysis
- Traffic Source Analysis
- Geographic Distribution
- Interactive filters

https://public.tableau.com/views/Book1_17830071008490/GA4E-commerceProductAnalytics?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link

---

# 🌐 Deployment

The Streamlit application is containerized with Docker and deployed on **Google Cloud Run**.

Deployment workflow:

```text
Python
   │
   ▼
Docker
   │
   ▼
Google Cloud Run
   │
   ▼
Public Web Application
```

Live application:

https://ga4-product-analytics-331058043654.europe-west9.run.app

---

# 📌 Key Business Insights

- The largest drop-off occurs between **View Item** and **Add to Cart**.
- Mobile devices generate the highest traffic volume.
- Checkout completion varies significantly across acquisition channels.
- Engagement metrics are strong predictors of purchase intent.
- High-intent users can be identified before completing checkout, enabling targeted interventions.

---

# 📁 Repository Contents

| Folder | Description |
|---------|-------------|
| `notebooks/` | Exploratory analysis and machine learning |
| `dbt/` | Data transformation pipeline |
| `app/` | Streamlit application |
| `src/` | BigQuery service layer |
| `tableau/` | Tableau dashboards |
| `models/` | Trained machine learning models |
| `outputs/` | Model evaluation results |

---

# 📚 Future Improvements

- Real-time GA4 streaming with BigQuery
- A/B testing framework
- Customer Lifetime Value prediction
- Product recommendation system
- SHAP model explainability
- FastAPI prediction service
- CI/CD pipeline with GitHub Actions

---

# 👤 Author

**Zhiwen MO**

Product Analytics • Data Analytics • Machine Learning • Business Intelligence