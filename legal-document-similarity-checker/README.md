# Legal Document Similarity Checker

## Overview
The Legal Document Similarity Checker is a project designed to facilitate the uploading, querying, and analysis of legal documents such as contracts and policies. The application allows users to upload mock documents, query specific clauses, and find semantically similar sections using advanced NLP techniques.

## Project Structure
```
legal-document-similarity-checker
├── data
│   ├── raw                # Directory for raw uploaded documents
│   ├── processed          # Directory for processed data
│   │   └── clean.jsonl    # Unified cleaned data in JSON Lines format
├── src
│   ├── app.py            # Main entry point for the application
│   ├── upload
│   │   └── uploader.py    # Handles document uploads
│   ├── query
│   │   └── query_handler.py # Manages clause querying
│   ├── similarity
│   │   └── similarity_checker.py # Finds semantically similar sections
│   ├── pipeline
│   │   └── data_pipeline.py # Data processing pipeline
│   └── utils
│       └── helpers.py      # Utility functions
├── tests
│   ├── test_uploader.py    # Unit tests for uploader functionality
│   ├── test_query_handler.py # Unit tests for query handling
│   ├── test_similarity_checker.py # Unit tests for similarity checking
│   └── test_data_pipeline.py # Unit tests for data processing
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation
└── .gitignore              # Files to ignore in version control
```

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   cd legal-document-similarity-checker
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Start the application:
   ```
   python src/app.py
   ```

2. Upload mock contracts or policies through the provided interface.

3. Query specific clauses (e.g., "termination conditions") to retrieve relevant sections.

4. Utilize the similarity checker to find semantically similar sections within the uploaded documents.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.