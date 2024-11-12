import ETL.extract as extract
import ETL.transform as transform
import ETL.load as load
import pandas as pd
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("etl_pipeline.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def run_pipeline():
    logger.info("Starting ETL pipeline.")
    
    try:
        # Extract income data from NCES and GFW data
        nces_url = 'https://nces.ed.gov/programs/digest/d22/tables/xls/tabn102.30.xlsx'
        income_data_excel = extract.download_nces_income_data(nces_url)
        logger.info("Downloaded NCES income data successfully.")
        
        gfw_url = 'https://gfw2-data.s3.amazonaws.com/country-pages/country_stats/download/2023/USA.xlsx'
        gfw_data_excel = extract.download_gfw_data(gfw_url)
        logger.info("Downloaded GFW data successfully.")
        
    except Exception as e:
        logger.error(f"Error during data extraction: {e}")
        return

    try:
        # Transform data
        income_cleaned_df = transform.clean_income_data(income_data_excel)
        logger.info("Income data cleaned successfully.")
        logger.debug(f"Income DataFrame after cleaning:\n{income_cleaned_df.head()}")
        
        available_years = [col for col in income_cleaned_df.columns if col.isnumeric()]
        gfw_cleaned_df = transform.clean_gfw_data(gfw_data_excel, available_years)
        logger.info("GFW data cleaned successfully.")
        logger.debug(f"GFW DataFrame after cleaning:\n{gfw_cleaned_df.head()}")
        
        merged_df = transform.merge_data(income_cleaned_df, gfw_cleaned_df)
        logger.info("Data merged successfully.")
        logger.debug(f"Merged DataFrame:\n{merged_df.head()}")
        
    except Exception as e:
        logger.error(f"Error during data transformation: {e}")
        return

    try:
        # Load data into SQLite
        load.load_to_sqlite(merged_df)
        logger.info("Data loaded into SQLite successfully.")
        
    except Exception as e:
        logger.error(f"Error during data loading: {e}")

if __name__ == "__main__":
    run_pipeline()
