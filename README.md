# Banking Customer Behaviour & Loan Risk Analysis

## Project Overview

This project analyses banking customer behaviour, transaction activity, loan portfolio performance, and customer-level credit risk using the Berka Banking dataset.

The project follows an end-to-end analytical workflow using SQL for business analysis and Python for exploratory data analysis and visual validation.

The objective is not just to report historical banking activity, but to identify meaningful patterns that can support customer understanding, loan monitoring, transaction analysis, and risk management.

---

## Business Context

A retail bank manages large volumes of customer, account, transaction, card, standing-order, and loan data.

Individual records alone do not provide a complete understanding of customer behaviour or financial risk. By combining multiple banking datasets, this project examines how customers use their accounts, how money moves through the banking system, how loans perform, and where potential credit risk is concentrated.

---

## Business Objectives

- Understand customer demographics and account behaviour
- Analyse transaction activity and money movement
- Evaluate the loan portfolio and repayment performance
- Compare repayment behaviour across loan amount segments
- Identify regional credit-risk patterns
- Identify high-risk customers using loan status and loan amount
- Validate SQL findings using Python visualisations
- Translate analytical findings into business recommendations

---

## Dataset

The Berka Banking dataset contains eight relational tables:

| Dataset | Description |
|---|---|
| `account.csv` | Customer account information and district association |
| `client.csv` | Customer demographic information |
| `disp.csv` | Relationship between customers and accounts |
| `loan.csv` | Loan amount, duration, payments and repayment status |
| `trans.csv` | Transaction history, amounts, balances and transaction types |
| `order.csv` | Standing orders and scheduled payments |
| `card.csv` | Bank card information |
| `district.csv` | District-level demographic and regional information |

The tables were integrated through SQL to perform business analysis and were later validated using Python EDA.

---

## Project Workflow

1. **Berka Banking Dataset**
   ↓
2. **SQLite Database Setup**
   ↓
3. **Data Validation & Quality Checks**
   ↓
4. **Data Preparation**
   ↓
5. **SQL Business Analysis**
   ↓
6. **Python Exploratory Data Analysis**
   ↓
7. **Visual Validation**
   ↓
8. **Business Insights**
   ↓
9. **Business Recommendations**

---

## Tools & Technologies

- Python
- Pandas
- Matplotlib
- SQL
- SQLite
- Jupyter Notebook
- VS Code
- Git & GitHub

---

## Data Quality & Preparation

Before performing business analysis, the dataset was reviewed for:

- Table structure
- Record counts
- Duplicate identifiers
- Missing values
- Transaction-specific missing values
- Date formatting
- Categorical values

All reviewed identifier fields showed zero duplicate IDs.

The transaction table contained contextual missing values in fields such as `operation`, `k_symbol`, `bank`, and `account`. These were investigated rather than blindly removed or imputed.

The analysis also identified zero values in the transaction `account` field. Further investigation showed that these records were associated with withdrawal transactions, so they were retained and interpreted according to transaction context.

---

## SQL Analysis

SQL was used to answer business questions across four major areas:

### 1. Customer Behaviour

- Customer distribution by district
- Customer age segmentation
- Gender distribution
- Account usage patterns
- Statement frequency analysis

### 2. Transaction Behaviour

- Transaction volume by account
- Transaction amount analysis
- Transaction type analysis
- Money inflow and outflow
- High-activity accounts

### 3. Loan Portfolio Analysis

- Loan distribution by amount segment
- Loan repayment status
- Repayment behaviour across loan segments
- Loan portfolio concentration
- Regional loan-risk patterns

### 4. Customer Risk Analysis

- Identification of high-risk loan accounts
- Analysis of repayment status
- Loan amount exposure among risky customers
- Prioritisation of high-value problem loans

---

## Python EDA & Validation

Python was used to validate the major SQL findings through visual analysis.

The EDA focused on:

- Customer behaviour validation
- Loan portfolio validation
- Transaction behaviour validation
- Customer risk validation

This provided visual evidence for the patterns identified through SQL.

---

## Key Findings

### Customer Behaviour

The 60+ age group represents the largest customer segment with **1,254 customers**, followed by the Under 30 group with **1,188 customers**.

### Loan Portfolio

The **Below 100K** loan segment contains the highest number of loans with **305 loans**, followed by the 100K–199K segment with 192 loans and the 200K+ segment with 185 loans.

### Loan Repayment

Most borrowers are classified as **"Running contract – OK so far"**, indicating an overall healthy repayment pattern. A smaller group falls into repayment-problem categories.

### Transaction Activity

Transaction activity is concentrated among a limited number of highly active accounts. The most active account recorded **634 transactions** among the analysed high-activity accounts.

### Money Flow

Total inflow amounted to approximately **3.23 billion**, while total outflow amounted to approximately **3.03 billion**, indicating relatively balanced movement of funds.

Outflow transactions represented **61.65%** of total transaction activity, while inflow transactions represented **38.35%**.

### Customer Risk

The analysis identified **76 high-risk customers**:

- 45 customers with running contracts and outstanding debt
- 31 customers whose contracts finished without full repayment

Several high-value loans were also present within repayment-problem categories, making loan amount an important factor when prioritising credit-risk monitoring.

---

## Business Recommendations

1. Develop financial products and services targeted towards the large 60+ customer segment.

2. Maintain regular portfolio reviews for the Below 100K loan segment because it contains the highest number of loans.

3. Monitor customers with outstanding repayments early to reduce the possibility of long-term default.

4. Periodically review highly active customer accounts to identify unusual transaction behaviour.

5. Track inflow and outflow patterns regularly to strengthen cash-flow monitoring.

6. Consider customers with consistent repayment histories as potential candidates for future lending and long-term relationship development.

7. Prioritise high-value loans with repayment problems for closer monitoring and recovery actions.

---

## Project Outcome

This project demonstrates how SQL and Python can work together in a practical banking analytics workflow.

SQL was used to combine relational banking data and answer business questions, while Python was used to validate the findings through exploratory analysis and visualisations.

The final analysis provides a structured view of:

- Customer behaviour
- Account activity
- Transaction patterns
- Loan portfolio performance
- Repayment behaviour
- Regional risk
- Customer-level credit risk

The project shows how raw banking data can be transformed into actionable business insights that support customer segmentation, lending decisions, transaction monitoring, and credit-risk management.

---

## Repository Structure

```text
Berka-Banking-Customer-Behaviour-Loan-Risk-Analysis/
│
├── data/
│   ├── account.csv
│   ├── card.csv
│   ├── client.csv
│   ├── disp.csv
│   ├── district.csv
│   ├── loan.csv
│   ├── order.csv
│   └── trans.csv
│
├── notebooks/
│   └── 01_berka_banking_analysis.ipynb
│
├── powerbi/
│
├── sql/
│
├── docs/
│
└── README.md
