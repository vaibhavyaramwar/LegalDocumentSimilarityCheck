import unittest
from src.upload.uploader import Uploader

class TestUploader(unittest.TestCase):

    def setUp(self):
        self.uploader = Uploader()

    def test_upload_valid_file(self):
        # Simulate uploading a valid file
        result = self.uploader.upload("data/raw/mock_contract.pdf")
        self.assertTrue(result)

    def test_upload_invalid_file_type(self):
        # Simulate uploading an invalid file type
        result = self.uploader.upload("data/raw/mock_contract.txt")
        self.assertFalse(result)

    def test_upload_empty_file(self):
        # Simulate uploading an empty file
        result = self.uploader.upload("data/raw/empty_file.pdf")
        self.assertFalse(result)

    def test_file_saved_correctly(self):
        # Simulate uploading a valid file and check if it is saved
        self.uploader.upload("data/raw/mock_contract.pdf")
        self.assertTrue(self.uploader.is_file_saved("mock_contract.pdf"))

if __name__ == '__main__':
    unittest.main()