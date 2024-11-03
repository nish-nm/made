import requests
import zipfile
import io
import pandas as pd
import os

def download_and_extract_world_bank_data(url, extract_path='././data/world_bank_data'):
    """
    Downloads and extracts World Bank data ZIP file from the given URL.
    
    Parameters:
    - url (str): The download URL for the World Bank data.
    - extract_path (str): The path where the extracted files will be saved.
    
    Returns:
    - str: Path to the main CSV file containing data.
    """
    response = requests.get(url)
    with zipfile.ZipFile(io.BytesIO(response.content)) as z:
        z.extractall(extract_path)
    
    # Identify the main data CSV file (starts with 'API_' and ends with '.csv')
    for file in os.listdir(extract_path):
        if file.startswith('API_') and file.endswith('.csv'):
            return os.path.join(extract_path, file)
    return None

def load_world_bank_data(file_path):
    """
    Loads the World Bank CSV data into a Pandas DataFrame.
    
    Parameters:
    - file_path (str): The path to the CSV file.
    
    Returns:
    - pd.DataFrame: The loaded DataFrame.
    """
    return pd.read_csv(file_path, skiprows=4)

def download_gfw_data(url, save_path='././data/USA_deforestation.xlsx'):
    """
    Downloads GFW data from the given URL and saves it as an XLSX file.
    
    Parameters:
    - url (str): The download URL for the GFW data.
    - save_path (str): The path where the file will be saved.
    
    Returns:
    - pd.ExcelFile: The loaded ExcelFile object for further processing.
    """
    response = requests.get(url)
    with open(save_path, 'wb') as file:
        file.write(response.content)
    return pd.ExcelFile(save_path)

def main():
    # World Bank data extraction
    world_bank_url = 'https://api.worldbank.org/v2/en/country/USA?downloadformat=csv'
    wb_file_path = download_and_extract_world_bank_data(world_bank_url)
    if wb_file_path:
        wb_data_df = load_world_bank_data(wb_file_path)
        print("World Bank DataFrame loaded successfully.")
    
    # GFW data extraction
    gfw_url = 'https://gfw2-data.s3.amazonaws.com/country-pages/country_stats/download/2023/USA.xlsx'
    gfw_df = download_gfw_data(gfw_url)
    print("GFW Excel Sheet Names:", gfw_df.sheet_names)

if __name__ == "__main__":
    main()
