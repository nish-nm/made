import requests
import zipfile
import io
import pandas as pd
import os

def download_nces_income_data(url, save_path='../data/us_income_data.xlsx'):
    """
    Downloads NCES income data from the provided URL and saves it as an Excel file.

    Parameters:
    - url (str): The download URL for the NCES data.
    - save_path (str): The path to save the Excel file.

    Returns:
    - pd.ExcelFile: The loaded ExcelFile object for further processing.
    """
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    response = requests.get(url)
    with open(save_path, 'wb') as file:
        file.write(response.content)
    return pd.ExcelFile(save_path)



def download_gfw_data(url, save_path='../data/USA_deforestation.xlsx'):
    """
    Downloads the GFW data from a given URL and saves it as an Excel file.
    
    Parameters:
    - url (str): The download URL for the GFW data.
    - save_path (str): Path to save the downloaded Excel file.
    
    Returns:
    - pd.ExcelFile: The loaded ExcelFile object for further processing.
    """
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    response = requests.get(url)
    with open(save_path, 'wb') as file:
        file.write(response.content)
    return pd.ExcelFile(save_path)

# def main():
#     # World Bank data extraction
#     world_bank_url = 'https://api.worldbank.org/v2/en/country/USA?downloadformat=csv'
#     wb_file_path = download_and_extract_world_bank_data(world_bank_url)
#     if wb_file_path:
#         wb_data_df = load_world_bank_data(wb_file_path)
#         print("World Bank DataFrame loaded successfully.")
    
#     # GFW data download and load
#     gfw_url = 'https://gfw2-data.s3.amazonaws.com/country-pages/country_stats/download/2023/USA.xlsx'
#     gfw_data_excel = download_gfw_data(gfw_url)
#     print("GFW Excel Sheet Names:", gfw_data_excel.sheet_names)

# if __name__ == "__main__":
#     main()
