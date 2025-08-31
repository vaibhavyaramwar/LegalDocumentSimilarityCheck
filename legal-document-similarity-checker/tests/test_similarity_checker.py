import unittest
from src.similarity.similarity_checker import SimilarityChecker

class TestSimilarityChecker(unittest.TestCase):

    def setUp(self):
        self.similarity_checker = SimilarityChecker()

    def test_similarity_detection(self):
        # Example documents for testing
        doc1 = "The termination conditions are as follows: ..."
        doc2 = "In the event of termination, the following conditions apply: ..."
        
        # Check if the similarity checker identifies these as similar
        similarity_score = self.similarity_checker.check_similarity(doc1, doc2)
        self.assertGreater(similarity_score, 0.5)  # Assuming a threshold for similarity

    def test_empty_document(self):
        doc1 = ""
        doc2 = "This is a valid document."
        
        # Check similarity with an empty document
        similarity_score = self.similarity_checker.check_similarity(doc1, doc2)
        self.assertEqual(similarity_score, 0)  # No similarity expected

    def test_identical_documents(self):
        doc1 = "This is a test document."
        doc2 = "This is a test document."
        
        # Check similarity of identical documents
        similarity_score = self.similarity_checker.check_similarity(doc1, doc2)
        self.assertEqual(similarity_score, 1)  # Perfect similarity

if __name__ == '__main__':
    unittest.main()