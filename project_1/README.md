# Project: Analysis of Resumes from HeadHunter

## Table of Contents

1. [Project Description](#project-description)
2. [What problem does it solve?](#what-problem-does-it-solve)
3. [Brief information about the data](#brief-information-about-the-data)
4. [Stages of work on the project](#stages-of-work-on-the-project)
5. [Results](#results)
6. [Conclusions](#conclusions)
7. [Visualizations](#visualizations)

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

### Visualizations

- [Age](visualizations/age.html)
- [Experience](visualizations/experience.html)
- [relocation_vs_salary](visualizations/relocation_vs_salary.html)
- [salary_by_schedule](visualizations/salary_by_schedule.html)
- [salary_to_city](visualizations/salary_to_city.html)
- [salary_to_education_and_age](visualizations/salary_to_education_and_age.html)
- [salary_to_education](visualizations/salary_to_education.html)
- [salary_to_experience](visualizations/salary_to_experience.html)
- [salary_to_sex](visualizations/salary_to_sex.html)

:arrow_up: [to the table of contents](https://github.com/nikbeznosikov/data_science/tree/main/project_1/README.md#table-of-contents)
