# CSV ETL Project

## Overview
This project is a beginner Data Engineering ETL pipeline built using Python and pandas.

The pipeline extracts raw Titanic passenger data, transforms and cleans the dataset, and loads the cleaned data into a new CSV file.

---

## Project Objective
The goal of this project is to practice ETL concepts:

- Extract raw CSV data
- Clean missing values
- Remove duplicates
- Standardize column names
- Create derived features
- Save cleaned data
- Implement logging

---

## Dataset
Dataset used: Titanic passenger dataset

Original columns:

- PassengerId
- Survived
- Pclass
- Name
- Sex
- Age
- SibSp
- Parch
- Ticket
- Fare
- Cabin
- Embarked

---

## Transformations Performed

### Data Cleaning
- Removed duplicate rows
- Filled missing `age` values using median
- Filled missing `embarked` values using mode

### Feature Engineering
Created new column:

```python
family_size = sibsp + parch
```

### Removed Unnecessary Columns
Dropped:

- passengerid
- cabin
- name
- ticket
- sibsp
- parch

### Standardization
- Converted column names to lowercase

---

## Project Structure

```text
csv_etl_project/
│
├── data/
│   ├── raw/
│   │   └── titanic.csv
│   │
│   └── cleaned/
│       └── cleaned_titanic.csv
│
├── logs/
│   └── etl.log
│
├── main.ipynb
├── main.py
├── README.md
├── .gitignore
```

---

## Technologies Used
- Python
- pandas
- logging

---

## How to Run

Clone project:

```bash
git clone <your-repo-link>
```

Install dependency:

```bash
pip install pandas
```

Run ETL pipeline:

```bash
python main.py
```

---

## Output
Generated cleaned dataset:

```text
data/cleaned/cleaned_titanic.csv
```

Generated log file:

```text
logs/etl.log
```

---

## Sample Output Columns

```text
survived
pclass
sex
age
fare
embarked
family_size
```