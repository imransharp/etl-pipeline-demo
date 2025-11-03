from scripts.extract import extract_data
from scripts.transform import transform_data
from scripts.load import load_data

def run_etl():
    df = extract_data()
    df = transform_data(df)
    load_data(df)
    print("🚀 ETL Pipeline Completed Successfully")

if __name__ == "__main__":
    run_etl()
