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

## Power BI Dashboard

The final analysis was brought into Power BI as a three-page dashboard. SQL was used to explore and aggregate the banking data, while Python helped validate the patterns before the results were turned into interactive business views in Power BI.

### Page 1 — Banking Analysis

![Power BI Page 3](PowerBI/Screenshot%202026-08-24%20121917.png)

The first page gives a quick view of the loan and customer side of the dataset.

- 682 total loans with a total loan amount of 103M.
- The dashboard covers 5.369K customers.
- Hlm. Praha has the highest client count among the displayed districts, with 663 clients.
- Loan status C has the highest count at 403, followed by A (203), D (45) and B (31).
- Loan amount increases with longer loan duration, reaching 35M at 60 months.
- Loan amount is highest under status C at 69M.
- Customer distribution is almost evenly split by gender, with around 3.0K female and 2.3K male customers.

### Page 2 — Loan Performance & Risk Analysis

![Power BI Page 2](PowerBI/Screenshot%202026-08-24%20122027.png)

The second page moves from the overall loan picture into loan performance.

- Average loan amount is highest for status D at 0.25M, followed by C (0.17M), B (0.14M) and A (0.09M).
- Average loan amount rises with loan duration, from 54K at the shorter duration to 244K at 60 months.
- Hlm. Praha also leads the displayed districts by total loan amount at around 13M.
- The loan-status distribution changes across different loan durations, showing how portfolio composition shifts as duration increases.
- Status C carries the largest loan amount at 69M, well above A (19M), D (11M) and B (4M).
- The district-level status view helps compare how loan outcomes are distributed across the highest-value districts.

### Page 3 — Transaction Analysis

![Power BI Page 1](PowerBI/Screenshot%202026-08-24%20122106.png)

The final page focuses on transaction activity and adds the behavioural side of the analysis.

- Total transaction amount is 6.26bn across 1.05632M transactions.
- Average transaction amount is 5.92K.
- PRIJEM contributes the highest transaction amount at 3.2bn, followed by VYDAJ at 2.8bn and VYBER at 0.2bn.
- Transaction activity rises steadily from 0.03M in 1993 to 0.32M in 1998.
- VYDAJ has the highest transaction count at 0.63M, followed by PRIJEM at 0.41M and VYBER at 0.02M.
- VYBER is the most frequent operation in the displayed operation breakdown, while VKLAD and VYBER contribute the largest transaction amounts at around 2.4bn and 2.3bn.

### From Analysis to Dashboard

The dashboard was not treated as a separate analysis. The SQL work was used to identify and aggregate the relevant banking patterns, Python was used to examine and validate the results, and Power BI was then used to present those findings in a more practical visual form.

The three pages therefore move from **loan and customer overview → loan performance and risk → transaction behaviour**, giving a connected view of the banking data rather than isolated charts.

## Recommendations

- Give closer attention to customers associated with higher-risk loan statuses before extending additional credit.
- Monitor longer-duration loans carefully, as average loan amounts increase with loan duration.
- Review high-value districts separately because a small number of districts contribute a large share of the displayed loan portfolio.
- Track transaction activity over time to understand changes in customer banking behaviour.
- Use transaction type and operation-level patterns together when reviewing customer activity and portfolio movement.

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

##  Overall Business Recommendations

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
├── PowerBI/
│   ├── README.md
│   ├── Screenshot 2026-08-24 121917.png
│   ├── Screenshot 2026-08-24 122027.png
│   └── Screenshot 2026-08-24 122106.png
│
├── sql/
│
└── README.md