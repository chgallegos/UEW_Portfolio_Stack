import requests
import pandas as pd
from sqlalchemy import create_engine
import logging

# Configure logging
logging.basicConfig(
    filename='etl_pipeline.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# PostgreSQL database connection details
DB_USER = 'your_username'
DB_PASSWORD = 'your_password'
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'etl_db'

# API Endpoint
API_URL = 'https://jsonplaceholder.typicode.com/users'

def extract_data(api_url):
    """Extract data from the API."""
    logging.info('Starting data extraction...')
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        logging.info('Data extraction completed successfully.')
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error during data extraction: {e}")
        raise

def transform_data(data):
    """Transform the raw JSON data into a clean DataFrame."""
    logging.info('Starting data transformation...')
    try:
        df = pd.json_normalize(data)
        # Select relevant columns and rename them
        df = df[['id', 'name', 'email', 'address.city', 'company.name']].rename(
            columns={
                'id': 'user_id',
                'name': 'user_name',
                'email': 'user_email',
                'address.city': 'user_city',
                'company.name': 'company_name'
            }
        )
        # Add a new column for record creation timestamp
        df['created_at'] = pd.Timestamp.now()
        logging.info('Data transformation completed successfully.')
        return df
    except Exception as e:
        logging.error(f"Error during data transformation: {e}")
        raise

def load_data(df, db_details):
    """Load the transformed data into a PostgreSQL database."""
    logging.info('Starting data loading...')
    try:
        # Create database connection
        engine = create_engine(f"postgresql://{db_details['user']}:{db_details['password']}@{db_details['host']}:{db_details['port']}/{db_details['name']}")
        # Load data into PostgreSQL table
        df.to_sql('users', engine, if_exists='replace', index=False)
        logging.info('Data loading completed successfully.')
    except Exception as e:
        logging.error(f"Error during data loading: {e}")
        raise

def validate_data(df):
    """Validate the data for any missing or inconsistent values."""
    logging.info('Starting data validation...')
    try:
        if df.isnull().values.any():
            raise ValueError("Data contains missing values")
        logging.info('Data validation completed successfully.')
    except ValueError as e:
        logging.error(f"Data validation error: {e}")
        raise

if __name__ == '__main__':
    # ETL process execution
    try:
        # Step 1: Extract
        raw_data = extract_data(API_URL)

        # Step 2: Transform
        transformed_data = transform_data(raw_data)

        # Step 3: Validate
        validate_data(transformed_data)

        # Step 4: Load
        load_data(
            transformed_data,
            db_details={
                'user': DB_USER,
                'password': DB_PASSWORD,
                'host': DB_HOST,
                'port': DB_PORT,
                'name': DB_NAME
            }
        )
        logging.info('ETL process completed successfully.')
    except Exception as e:
        logging.error(f"ETL process failed: {e}")
