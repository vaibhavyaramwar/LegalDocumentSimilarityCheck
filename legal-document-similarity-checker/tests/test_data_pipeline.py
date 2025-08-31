import unittest
from src.pipeline.data_pipeline import DataPipeline

class TestDataPipeline(unittest.TestCase):

    def setUp(self):
        self.pipeline = DataPipeline()

    def test_process_raw_data(self):
        raw_data = [
            {"contract": "Contract A", "content": "This is the content of contract A."},
            {"contract": "Contract B", "content": "This is the content of contract B."}
        ]
        processed_data = self.pipeline.process_raw_data(raw_data)
        self.assertIsInstance(processed_data, list)
        self.assertGreater(len(processed_data), 0)

    def test_save_clean_data(self):
        clean_data = [
            {"contract": "Contract A", "cleaned_content": "Cleaned content of contract A."},
            {"contract": "Contract B", "cleaned_content": "Cleaned content of contract B."}
        ]
        result = self.pipeline.save_clean_data(clean_data)
        self.assertTrue(result)
        # Additional checks can be added to verify the content of clean.jsonl

    def test_load_raw_data(self):
        raw_data = self.pipeline.load_raw_data('data/raw/')
        self.assertIsInstance(raw_data, list)
        self.assertGreater(len(raw_data), 0)

if __name__ == '__main__':
    unittest.main()