class Uploader:
    def __init__(self, upload_directory):
        self.upload_directory = upload_directory

    def validate_file(self, file):
        # Implement validation logic (e.g., file type, size)
        if not file.name.endswith(('.pdf', '.docx', '.txt')):
            raise ValueError("Invalid file type. Only .pdf, .docx, and .txt files are allowed.")
        return True

    def save_file(self, file):
        if self.validate_file(file):
            file_path = f"{self.upload_directory}/{file.name}"
            with open(file_path, 'wb') as f:
                f.write(file.read())
            return file_path

    def upload(self, file):
        try:
            return self.save_file(file)
        except Exception as e:
            print(f"Error uploading file: {e}")
            return None