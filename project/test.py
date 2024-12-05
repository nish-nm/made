import os
import unittest
from pipeline import run_pipeline
from ETL.extract import download_nces_income_data, download_gfw_data

class TestDataPipeline(unittest.TestCase):

    def setUp(self):
        """
        Set up the test environment.
        Remove output files if they exist to ensure a clean test environment.
        """
        self.db_path = '../data/analysis.db'
        self.nces_file_path = '../data/us_income_data.xlsx'
        self.gfw_file_path = '../data/USA_deforestation.xlsx'

        # Clean up any pre-existing files
        for file_path in [self.db_path, self.nces_file_path, self.gfw_file_path]:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_pipeline_execution(self):
        """
        Validate:
        1. Downloaded files (NCES and GFW) exist.
        2. The SQLite database file is created.
        """
        nces_url = 'https://nces.ed.gov/programs/digest/d22/tables/xls/tabn102.30.xlsx'
        gfw_url = 'https://gfw2-data.s3.amazonaws.com/country-pages/country_stats/download/2023/USA.xlsx'

        download_nces_income_data(nces_url, save_path=self.nces_file_path)
        download_gfw_data(gfw_url, save_path=self.gfw_file_path)

        self.assertTrue(os.path.exists(self.nces_file_path), "NCES income data file was not downloaded.")
        self.assertTrue(os.path.exists(self.gfw_file_path), "GFW data file was not downloaded.")

        run_pipeline()
        self.assertTrue(os.path.exists(self.db_path), "Database file was not created by the pipeline.")

    def tearDown(self):
        """
        Clean up the test environment.
        """
        for file_path in [self.db_path, self.nces_file_path, self.gfw_file_path]:
            if os.path.exists(file_path):
                os.remove(file_path)

if __name__ == '__main__':
    unittest.main()
