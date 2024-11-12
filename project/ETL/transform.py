# import pandas as pd
# import os
# def load_world_bank_files(folder_path):
#     """
#     Loads the three main World Bank files into separate DataFrames.
    
#     Parameters:
#     - folder_path (str): Path to the folder containing the World Bank CSV files.
    
#     Returns:
#     - dict: A dictionary with keys 'main_data', 'country_metadata', 'indicator_metadata' pointing to DataFrames.
#     """
#     files = os.listdir(folder_path)
    
#     main_data_file = [f for f in files if 'API_' in f][0]
#     country_metadata_file = [f for f in files if 'Metadata_Country' in f][0]
#     indicator_metadata_file = [f for f in files if 'Metadata_Indicator' in f][0]
    
#     main_data_df = pd.read_csv(os.path.join(folder_path, main_data_file), skiprows=4)
#     country_metadata_df = pd.read_csv(os.path.join(folder_path, country_metadata_file))
#     indicator_metadata_df = pd.read_csv(os.path.join(folder_path, indicator_metadata_file))
    
#     return {
#         'main_data': main_data_df,
#         'country_metadata': country_metadata_df,
#         'indicator_metadata': indicator_metadata_df
#     }

# def transform_data(df, columns_to_keep, rename_columns=None, drop_na=True):
#     """
#     Transforms the DataFrame by keeping only necessary columns, optionally renaming them,
#     and dropping rows with null values if specified.
    
#     Parameters:
#     - df (pd.DataFrame): The input DataFrame.
#     - columns_to_keep (list): List of column names to retain.
#     - rename_columns (dict): Dictionary for renaming columns (optional).
#     - drop_na (bool): Whether to drop rows with null values (default is True).
    
#     Returns:
#     - pd.DataFrame: Transformed DataFrame with only necessary columns.
#     """
#     # Keep only the specified columns
#     transformed_df = df[columns_to_keep]
    
#     # Rename columns if rename_columns is provided
#     if rename_columns:
#         transformed_df.rename(columns=rename_columns, inplace=True)
    
#     # Check for null values and drop them if drop_na is True
#     if drop_na:
#         null_count = transformed_df.isnull().sum().sum()
#         if null_count > 0:
#             print(f"Found {null_count} null values. Dropping rows with null values.")
#             transformed_df.dropna(inplace=True)
#         else:
#             print("No null values found.")
    
#     return transformed_df

# def main():
#     # Path to the folder containing the World Bank files
#     folder_path = '././data/world_bank_data'
    
#     # Load the data
#     wb_data = load_world_bank_files(folder_path)
#     main_data_df = wb_data['main_data']
    
#     # Specify necessary columns for transformation
#     wb_columns_to_keep = ['Country Name', 'Indicator Name', 'Indicator Code', '2021']
    
#     # Optional renaming of columns for consistency
#     wb_rename_columns = {'Country Name': 'Country', '2021': 'Value_2021'}
    
#     # Transform main data
#     wb_transformed = transform_data(main_data_df, wb_columns_to_keep, wb_rename_columns)
#     gfw_file_path = '././data/USA_deforestation.xlsx'

#     gfw_df = pd.read_excel(gfw_file_path, sheet_name='Country tree cover loss')  # Example sheet

#     # Specify necessary columns for transformation
#     wb_columns_to_keep = ['Country Name', 'Indicator Name', 'Indicator Code', '2021']
#     gfw_columns_to_keep = ['Region', 'Tree cover loss', 'CO2 emissions']

#     # Optional renaming of columns for consistency
#     wb_rename_columns = {'Country Name': 'Country', '2021': 'Value_2021'}
#     gfw_rename_columns = {'Tree cover loss': 'Tree_Cover_Loss', 'CO2 emissions': 'CO2_Emissions'}

#     gfw_transformed = transform_data(gfw_df, gfw_columns_to_keep, gfw_rename_columns)

#     # Save transformed data to CSV for the next step
#     wb_transformed.to_csv('wb_transformed.csv', index=False)
#     gfw_transformed.to_csv('gfw_transformed.csv', index=False)

#     print("Data transformation completed and saved to CSV files.")

# if __name__ == "__main__":
#     main()


import pandas as pd

def clean_income_data(excel_file):
    """
    Cleans the NCES income data to prepare for merging. Extracts relevant columns and rows for state-level income,
    keeps all year columns, and removes unnamed columns.

    Parameters:
    - excel_file (pd.ExcelFile): Excel file containing NCES income data.

    Returns:
    - pd.DataFrame: Cleaned DataFrame with state-level income data across multiple years.
    """
    income = pd.read_excel(excel_file, skiprows=2)

    # Ensure all column names are strings to avoid issues with NaN or non-string types
    income.columns = income.columns.map(str)

    # Remove unnamed columns
    income_df = income.loc[:, ~income.columns.str.contains('^Unnamed')]

    # Drop specific rows by index
    income_df = income_df.drop([0, 53, 54, 55, 56], axis=0)

    # Rename columns to match desired format for years
    income_df = income_df.rename(columns={
        "State": "State",         
        '1990\\1\\': "1990",          
        '2000\\2\\': "2000",
        "2005": "2005",
        "2010": "2010",
        "2015": "2015",
        "2020": "2020",
        "2021": "2021"
    })
    
    return income_df

def clean_gfw_data(excel_file, available_years):
    """
    Extracts relevant yearly deforestation and CO₂ data from the GFW Excel file at the state level,
    keeps only the years available in the income data, and removes unnamed columns.

    Parameters:
    - excel_file (pd.ExcelFile): Excel file containing GFW data.
    - available_years (list): List of years to keep in GFW data based on availability in income data.

    Returns:
    - pd.DataFrame: Cleaned DataFrame with state-level yearly deforestation and CO₂ data.
    """
    # Load necessary sheets
    tree_loss_df = excel_file.parse('Subnational 1 tree cover loss')
    carbon_df = excel_file.parse('Subnational 1 carbon data')

    # # Remove unnamed columns
    # tree_loss_df = tree_loss_df.loc[:, ~tree_loss_df.columns.str.contains('^Unnamed')]
    # carbon_df = carbon_df.loc[:, ~carbon_df.columns.str.contains('^Unnamed')]

    # Select columns that match the years in available_years
    tree_loss_columns = ['subnational1'] + [f'tc_loss_ha_{year}' for year in available_years if f'tc_loss_ha_{year}' in tree_loss_df.columns]
    carbon_columns = ['subnational1'] + [f'gfw_forest_carbon_gross_emissions_{year}__Mg_CO2e' for year in available_years if f'gfw_forest_carbon_gross_emissions_{year}__Mg_CO2e' in carbon_df.columns]

    # Filter the dataframes to keep only necessary columns
    tree_loss_df = tree_loss_df[tree_loss_columns]
    carbon_df = carbon_df[carbon_columns]

    # Rename 'subnational1' to 'State' for consistency
    tree_loss_df = tree_loss_df.rename(columns={'subnational1': 'State'})
    carbon_df = carbon_df.rename(columns={'subnational1': 'State'})

    # Merge tree loss and carbon data on state
    merged_gfw_df = pd.merge(tree_loss_df, carbon_df, on='State', how='inner')
    
    # Fill missing values if needed
    merged_gfw_df = merged_gfw_df.dropna()
    
    return merged_gfw_df

def merge_data(income_df, gfw_df):
    """
    Merges income data with GFW environmental data at the state level.

    Parameters:
    - income_df (pd.DataFrame): Cleaned income DataFrame.
    - gfw_df (pd.DataFrame): Cleaned GFW DataFrame with state-level data.

    Returns:
    - pd.DataFrame: Merged DataFrame at the state level with unnamed columns removed.
    """
    # Merge on 'State' column
    merged_df = pd.merge(income_df, gfw_df, on='State', how='inner')
    
    # Remove any unnamed columns in the merged DataFrame
    merged_df = merged_df.loc[:, ~merged_df.columns.str.contains('^Unnamed')]
    
    # Fill any remaining missing values
    merged_df = merged_df.dropna()
    
    return merged_df

