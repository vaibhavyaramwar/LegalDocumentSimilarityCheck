from src.query.query_handler import QueryHandler

def test_query_handler_initialization():
    query_handler = QueryHandler()
    assert query_handler is not None

def test_query_clauses():
    query_handler = QueryHandler()
    mock_data = {
        "contract": "This is a sample contract with termination conditions.",
        "clauses": {
            "termination": "The contract may be terminated by either party with a 30-day notice."
        }
    }
    query_handler.load_data(mock_data)
    result = query_handler.query_clause("termination")
    assert result == "The contract may be terminated by either party with a 30-day notice."

def test_semantic_similarity():
    query_handler = QueryHandler()
    mock_data = {
        "contract": "This contract includes termination conditions and renewal options.",
        "clauses": {
            "termination": "The contract may be terminated by either party with a 30-day notice.",
            "renewal": "The contract can be renewed upon mutual agreement."
        }
    }
    query_handler.load_data(mock_data)
    similar_sections = query_handler.find_semantically_similar("termination conditions")
    assert len(similar_sections) > 0  # Assuming there are similar sections found

def test_empty_query():
    query_handler = QueryHandler()
    result = query_handler.query_clause("nonexistent clause")
    assert result is None  # Expecting None for a clause that doesn't exist