import pandas as pd
import logging as log

log.basicConfig(
    filename="./logs/etl.log",
    level=log.INFO,
    format="%(asctime)s- %(levelname)s - %(message)s"
)

def extract():
    log.info("Starting data extraction")
    df = pd.read_csv("./data/raw/titanic.csv")
    log.info(f"Dataset loaded successfully with {len(df)} rows")
    return df

def transform(df):
    log.info("Starting transformation")
    before_rows = len(df)
    df = df.drop_duplicates()
    after_rows = len(df)
    log.info(f"Removed {before_rows - after_rows} duplicate rows")
    
    df.columns = df.columns.str.lower()
    log.info("Standardized column names")
    
    df["family_size"] = df["sibsp"] + df["parch"]
    log.info("Created family_size column")
    
    cols_to_drop = ["name","ticket" ,"passengerid","cabin" ,"sibsp","parch"]
    df = df.drop(columns=cols_to_drop)
    log.info("Dropped unnecessary columns")
    
    median_age = df["age"].median()
    df["age"] = df["age"].fillna(median_age)
    log.info("Filled missing age values using median")
    
    most_common_port = df["embarked"].mode()[0]
    df["embarked"] = df["embarked"].fillna(most_common_port)
    log.info("Filled missing embarked values using mode")
    
    log.info("Transformation completed")
    return df

def load(df):
    log.info("Saving cleaned dataset")
    df.to_csv("./data/cleaned/cleaned_titanic.csv", index=False)
    log.info("Cleaned dataset saved successfully")


def main():
    log.info("ETL pipeline started")
    
    df =extract()
    df = transform(df)
    df = load(df)
    
    log.info("ETL pipeline completed")
    
if __name__ == "__main__":
    main()    