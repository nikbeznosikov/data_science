## Project: Data Analysis and Modeling for Bank Deposits

### Table of Contents

1. [Project Description](#project-description)
2. [What problem does it solve?](#what-problem-does-it-solve)
3. [Brief information about the data](#brief-information-about-the-data)
4. [Stages of work on the project](#stages-of-work-on-the-project)
5. [Results](#results)
6. [Conclusions](#conclusions)

### Project Description

This project involves analyzing a dataset of bank customers to predict whether they will open a deposit based on various factors such as age, job, marital status, and other financial indicators. The analysis includes data preprocessing, feature engineering, and the use of machine learning models such as logistic regression and decision trees. The goal is to create a model that can accurately classify customers into those who will or will not open a deposit.

:arrow_up: [to the table of contents](#table-of-contents)

### What problem does it solve?

The project aims to predict customer behavior related to opening a bank deposit. This involves analyzing various factors like age, education, marital status, and job type to determine how these features influence the decision to open a deposit.

**Steps involved:**

1. Feature engineering to transform categorical variables (e.g., job, education, marital status) into dummy variables.
2. Data cleaning, handling missing values in `balance`, `job`, and `education` by replacing them with median and mode, respectively.
3. Building and training machine learning models, including logistic regression and decision trees, to classify customers.

**What do we practice?**

- Feature engineering (e.g., dummy variables, creating age groups)
- Data cleaning (handling missing values, removing outliers)
- Training and evaluating machine learning models, including logistic regression and decision trees

### Brief information about the data

The dataset consists of various features related to bank customers, such as:

- **Demographic information**: age, job, marital status, education
- **Financial indicators**: balance, housing loan, personal loan
- **Contact details**: type of last contact, month of last contact, day of the last contact, and duration of contact
- **Marketing data**: number of previous contacts, results of previous marketing campaigns

The goal is to predict whether a customer will open a deposit (the target variable: `deposit`).

### Stages of work on the project

1. **Data Preprocessing**:

   - Handling missing values in the `balance`, `job`, and `education` columns by using median and mode imputation.
   - Removing outliers in the `balance` feature using the Tukey method.

2. **Feature Engineering**:

   - Converting categorical variables (e.g., `job`, `marital`, `contact`) into dummy variables using `pd.get_dummies`.
   - Creating age groups to understand how age affects the likelihood of opening a deposit.
   - Normalizing numerical features using `MinMaxScaler`.

3. **Model Training**:
   - **Logistic Regression**: Used as a baseline model for binary classification.
   - **Decision Trees**: Trained with `max_depth` tuning to prevent overfitting.

### Results

The project resulted in the creation of predictive models using both logistic regression and decision trees. The logistic regression model was effective in capturing the relationships between features and the target variable, while the decision tree model provided interpretable rules for classification. Feature engineering, such as creating age groups and handling categorical variables, improved model performance.

### Conclusions

- **Logistic Regression** and **Decision Trees** both showed strong performance in predicting deposit openings, with logistic regression providing slightly better generalization on test data.
- Key factors influencing the decision to open a deposit include the duration of the last contact, job type, and whether the customer has a loan.
- Clients in the `management` and `technical professions` are more likely to open deposits, while `self-employed` and `housemaids` are less likely.
- Customers with housing loans are less likely to open deposits compared to those without loans.
- Future improvements could involve trying ensemble methods like **Random Forest** or **Gradient Boosting** to improve classification accuracy.

:arrow_up: [to the table of contents](#table-of-contents)
