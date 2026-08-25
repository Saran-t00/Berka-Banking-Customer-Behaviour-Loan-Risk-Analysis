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

## Dataset

The Berka Banking dataset contains eight relational tables covering customer information, accounts, loans, transactions, cards, standing orders, customer-account relationships, and district-level information.

| Dataset | Rows | Columns | Description |
|---|---:|---:|---|
| `account.csv` | 4,500 | 4 | Customer account information, including district, account frequency, and account opening date |
| `client.csv` | 5,369 | 3 | Customer information, including birth number and district association |
| `disp.csv` | 5,369 | 4 | Relationship between customers and bank accounts |
| `loan.csv` | 682 | 7 | Loan information including amount, duration, payments, and loan status |
| `trans.csv` | 1,056,320 | 10 | Transaction history including transaction type, operation, amount, balance, and related accounts |
| `order.csv` | 6,471 | 6 | Standing orders and scheduled payment information |
| `card.csv` | 892 | 4 | Bank card information linked to customer-account relationships |
| `district.csv` | 77 | 16 | District-level demographic and regional information |

The tables were integrated through relational keys and analysed using SQL, Python, and Power BI.

---

## Data Schema

### 1. account.csv

| Column | Data Type | Description |
|---|---|---|
| `account_id` | Integer | Unique identifier of the bank account |
| `district_id` | Integer | Identifier of the district associated with the account |
| `frequency` | Text | Frequency of account statements/payments |
| `date` | Integer | Account creation date in the original dataset format |

---

### 2. client.csv

| Column | Data Type | Description |
|---|---|---|
| `client_id` | Integer | Unique identifier of the customer |
| `birth_number` | Integer | Customer birth number in the original dataset format |
| `district_id` | Integer | Identifier of the district associated with the customer |

---

### 3. disp.csv

| Column | Data Type | Description |
|---|---|---|
| `disp_id` | Integer | Unique identifier of the customer-account relationship |
| `client_id` | Integer | Identifier of the customer |
| `account_id` | Integer | Identifier of the bank account |
| `type` | Text | Relationship type between customer and account |

**Common values:**
- `OWNER` — Account owner
- `DISPONENT` — Authorized account user

---

### 4. loan.csv

| Column | Data Type | Description |
|---|---|---|
| `loan_id` | Integer | Unique identifier of the loan |
| `account_id` | Integer | Identifier of the account associated with the loan |
| `date` | Integer | Loan issue date in the original dataset format |
| `amount` | Integer | Total loan amount |
| `duration` | Integer | Loan duration in months |
| `payments` | Decimal | Monthly loan payment amount |
| `status` | Text | Current or final loan status |

**Loan status codes:**
- `A` — Finished, no problems
- `B` — Finished, loan not fully paid
- `C` — Running, no problems
- `D` — Running, client in debt

---

### 5. trans.csv

| Column | Data Type | Description |
|---|---|---|
| `trans_id` | Integer | Unique identifier of the transaction |
| `account_id` | Integer | Identifier of the account involved in the transaction |
| `date` | Integer | Transaction date in the original dataset format |
| `type` | Text | Transaction direction/type |
| `operation` | Text | Specific transaction operation |
| `amount` | Decimal | Transaction amount |
| `balance` | Decimal | Account balance after the transaction |
| `k_symbol` | Text | Transaction classification/category |
| `bank` | Text | Related bank code |
| `account` | Decimal | Related account identifier |

**Transaction type meanings:**
- `PRIJEM` — Credit / Money received
- `VYDAJ` — Debit / Money spent
- `VYBER` — Cash withdrawal

**Operation meanings:**
- `VKLAD` — Cash deposit
- `PREVOD Z UCTU` — Transfer from another account
- `VYBER` — Cash withdrawal
- `PREVOD NA UCET` — Transfer to another account
- `VYBER KARTOU` — Card withdrawal

---

### 6. order.csv

| Column | Data Type | Description |
|---|---|---|
| `order_id` | Integer | Unique identifier of the standing order |
| `account_id` | Integer | Identifier of the account issuing the order |
| `bank_to` | Text | Destination bank code |
| `account_to` | Integer | Destination account identifier |
| `amount` | Decimal | Standing order amount |
| `k_symbol` | Text | Purpose/category of the payment |

---

### 7. card.csv

| Column | Data Type | Description |
|---|---|---|
| `card_id` | Integer | Unique identifier of the bank card |
| `disp_id` | Integer | Customer-account relationship identifier |
| `type` | Text | Type of bank card |
| `issued` | Text | Card issue date in the original dataset format |

**Card types:**
- `classic` — Classic card
- `junior` — Junior card
- `gold` — Gold card

---

### 8. district.csv

| Column | Data Type | Description |
|---|---|---|
| `A1` | Integer | District identifier |
| `A2` | Text | District name |
| `A3` | Text | Region |
| `A4` | Integer | Population |
| `A5` | Integer | Number of municipalities with less than 499 inhabitants |
| `A6` | Integer | Number of municipalities with 500–1,999 inhabitants |
| `A7` | Integer | Number of municipalities with 2,000–9,999 inhabitants |
| `A8` | Integer | Number of municipalities with more than 10,000 inhabitants |
| `A9` | Integer | Number of cities |
| `A10` | Decimal | Ratio of urban inhabitants |
| `A11` | Integer | Average salary |
| `A12` | Text | Unemployment rate |
| `A13` | Decimal | Ratio of entrepreneurs |
| `A14` | Integer | Number of crimes in the district |
| `A15` | Text | Unemployment rate in the district |
| `A16` | Integer | Number of crimes in the previous year |

---

## Key Relationships

The main relationships between the tables are:

- `account.account_id` → `disp.account_id`
- `account.account_id` → `loan.account_id`
- `account.account_id` → `trans.account_id`
- `account.account_id` → `order.account_id`
- `client.client_id` → `disp.client_id`
- `client.district_id` → `district.A1`
- `disp.disp_id` → `card.disp_id`

These relationships allow customer, account, loan, transaction, card, and district information to be combined for business analysis.

---

## Dataset Summary

The dataset contains:

- **5,369 customers**
- **4,500 accounts**
- **682 loans**
- **1,056,320 transactions**
- **6,471 standing orders**
- **892 bank cards**
- **5,369 customer-account relationships**
- **77 districts**

The dataset provides the foundation for analysing customer behaviour, loan performance, transaction activity, account usage, and regional banking patterns.

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
- Power BI
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

![Power BI Page 3](PowerBI/Screenshot%202026-08-25%20133055.png)

The first page gives a quick view of the loan and customer side of the dataset.

- 682 total loans with a total loan amount of 103M.
- The dashboard covers 5.369K customers.
- Hlm. Praha has the highest client count among the displayed districts, with 663 clients.
- Loan status C has the highest count at 403, followed by A (203), D (45) and B (31).
- Loan amount increases with longer loan duration, reaching 35M at 60 months.
- Loan amount is highest under status C at 69M.
- Customer distribution is almost evenly split by gender, with around 2645 female and 2724 male customers.

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

## Repository Structure

```text
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
│   ├── Screenshot 2026-08-25 133055.png
│   ├── Screenshot 2026-08-24 122027.png
│   └── Screenshot 2026-08-24 122106.png
│
├── sql//
│
└── README.md
```
