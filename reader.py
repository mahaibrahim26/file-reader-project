class FileReader:
    def __init__(self, filename):
        self._filename = filename
        self._content = None

    @property
    def filename(self):
        return self._filename

    @filename.setter
    def filename(self, new_name):
        self._filename = new_name

    def read_file(self):
        with open(self._filename, 'r') as f:
            for line in f:
                yield line.strip()

    def get_content(self):
        self._content = "\n".join([line for line in self.read_file()])
        return self._content

    def __str__(self):
        return f"FileReader for '{self._filename}'"

    def __add__(self, other):
        return self.get_content() + "\n" + other.get_content()

    @staticmethod
    def description():
        return "Reads files using a generator"

    @classmethod
    def from_file(cls, path):
        return cls(path)