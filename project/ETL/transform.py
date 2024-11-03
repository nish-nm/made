import pandas as pd
import os
def load_world_bank_files(folder_path):
    """
    Loads the three main World Bank files into separate DataFrames.
    
    Parameters:
    - folder_path (str): Path to the folder containing the World Bank CSV files.
    
    Returns:
    - dict: A dictionary with keys 'main_data', 'country_metadata', 'indicator_metadata' pointing to DataFrames.
    """
    files = os.listdir(folder_path)
    
    main_data_file = [f for f in files if 'API_' in f][0]
    country_metadata_file = [f for f in files if 'Metadata_Country' in f][0]
    indicator_metadata_file = [f for f in files if 'Metadata_Indicator' in f][0]
    
    main_data_df = pd.read_csv(os.path.join(folder_path, main_data_file), skiprows=4)
    country_metadata_df = pd.read_csv(os.path.join(folder_path, country_metadata_file))
    indicator_metadata_df = pd.read_csv(os.path.join(folder_path, indicator_metadata_file))
    
    return {
        'main_data': main_data_df,
        'country_metadata': country_metadata_df,
        'indicator_metadata': indicator_metadata_df
    }

def transform_data(df, columns_to_keep, rename_columns=None, drop_na=True):
    """
    Transforms the DataFrame by keeping only necessary columns, optionally renaming them,
    and dropping rows with null values if specified.
    
    Parameters:
    - df (pd.DataFrame): The input DataFrame.
    - columns_to_keep (list): List of column names to retain.
    - rename_columns (dict): Dictionary for renaming columns (optional).
    - drop_na (bool): Whether to drop rows with null values (default is True).
    
    Returns:
    - pd.DataFrame: Transformed DataFrame with only necessary columns.
    """
    # Keep only the specified columns
    transformed_df = df[columns_to_keep]
    
    # Rename columns if rename_columns is provided
    if rename_columns:
        transformed_df.rename(columns=rename_columns, inplace=True)
    
    # Check for null values and drop them if drop_na is True
    if drop_na:
        null_count = transformed_df.isnull().sum().sum()
        if null_count > 0:
            print(f"Found {null_count} null values. Dropping rows with null values.")
            transformed_df.dropna(inplace=True)
        else:
            print("No null values found.")
    
    return transformed_df

def main():
    # Path to the folder containing the World Bank files
    folder_path = '././data/world_bank_data'
    
    # Load the data
    wb_data = load_world_bank_files(folder_path)
    main_data_df = wb_data['main_data']
    
    # Specify necessary columns for transformation
    wb_columns_to_keep = ['Country Name', 'Indicator Name', 'Indicator Code', '2021']
    
    # Optional renaming of columns for consistency
    wb_rename_columns = {'Country Name': 'Country', '2021': 'Value_2021'}
    
    # Transform main data
    wb_transformed = transform_data(main_data_df, wb_columns_to_keep, wb_rename_columns)
    gfw_file_path = '././data/USA_deforestation.xlsx'

    gfw_df = pd.read_excel(gfw_file_path, sheet_name='Country tree cover loss')  # Example sheet

    # Specify necessary columns for transformation
    wb_columns_to_keep = ['Country Name', 'Indicator Name', 'Indicator Code', '2021']
    gfw_columns_to_keep = ['Region', 'Tree cover loss', 'CO2 emissions']

    # Optional renaming of columns for consistency
    wb_rename_columns = {'Country Name': 'Country', '2021': 'Value_2021'}
    gfw_rename_columns = {'Tree cover loss': 'Tree_Cover_Loss', 'CO2 emissions': 'CO2_Emissions'}

    gfw_transformed = transform_data(gfw_df, gfw_columns_to_keep, gfw_rename_columns)

    # Save transformed data to CSV for the next step
    wb_transformed.to_csv('wb_transformed.csv', index=False)
    gfw_transformed.to_csv('gfw_transformed.csv', index=False)

    print("Data transformation completed and saved to CSV files.")

if __name__ == "__main__":
    main()
