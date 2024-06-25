# Project: Analysis of Resumes from HeadHunter

## Table of Contents

1. [Project Description](https://github.com/nikbeznosikov/data_science/tree/main/project_1/README.md#project-description)
2. [What problem does it solve?](https://github.com/nikbeznosikov/data_science/tree/main/project_1/README.md#what-problem-does-it-solve)
3. [Brief information about the data](https://github.com/nikbeznosikov/data_science/tree/main/project_1/README.md#brief-information-about-the-data)
4. [Stages of work on the project](https://github.com/nikbeznosikov/data_science/tree/main/project_1/README.md#stages-of-work-on-the-project)
5. [Results](https://github.com/nikbeznosikov/data_science/tree/main/project_1/README.md#results)
6. [Conclusions](https://github.com/nikbeznosikov/data_science/tree/main/project_1/README.md#conclusions)

### Project Description

This project involves analyzing resume data from HeadHunter to understand various patterns and insights about job seekers.

:arrow_up: [to the table of contents](#table-of-contents)

### What problem does it solve?

The project aims to clean and analyze resume data to extract meaningful insights about the education, work experience, and other attributes of job seekers.

**Steps involved:**

1. Read and inspect the data.
2. Transform key features such as education level and age.
3. Clean the data by handling duplicates, missing values, and outliers.
4. Visualize key data points to gain insights.

**What do we practice?**

- Data cleaning and preprocessing
- Exploratory data analysis
- Feature transformation and extraction
- Data visualization

### Brief information about the data

The data consists of resumes from HeadHunter, with various features such as education, work experience, gender, age, and salary expectations.

### Stages of work on the project

1. **Data Inspection**: Read the data using Pandas, inspect the first few rows, and understand the structure of the dataset.
2. **Feature Transformation**:
   - Extract education level from the "Образование и ВУЗ" column.
   - Parse the "Пол, возраст" column to separate gender, age, and birth date.
3. **Data Cleaning**:
   - Remove duplicate entries.
   - Handle missing values by filling or removing as appropriate.
   - Remove outliers based on salary and age.
4. **Data Visualization**:
   - Created histograms to visualize the distribution of ages and salaries.
   - Built bar charts to show the frequency of different education levels.
   - Used scatter plots to explore the relationship between experience and age.

### Results

The project resulted in a clean dataset ready for further analysis or modeling. Key transformations and cleaning steps were performed to ensure data quality. Visualizations provided insights into the data distribution and relationships between different features.

### Conclusions

- Extracting structured information from complex text fields is crucial for analysis.
- Proper handling of missing values and outliers can significantly improve data quality.
- Visualizations help in understanding data distributions and relationships.
- The cleaned and transformed dataset provides a solid foundation for more detailed analysis or machine learning tasks.

:arrow_up: [to the table of contents](https://github.com/nikbeznosikov/data_science/tree/main/project_1/README.md#table-of-contents)
