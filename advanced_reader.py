from reader import FileReader

class AdvancedReader(FileReader):
    def __init__(self, filename):
        super().__init__(filename)

    def combine_files(self, file_list):
        """Combine contents of multiple files into one string."""
        combined = ""
        for file in file_list:
            reader = FileReader(file)
            combined += reader.get_content() + "\n"
        return combined.strip()

    def __str__(self):
        return f"AdvancedReader handling '{self.filename}'"