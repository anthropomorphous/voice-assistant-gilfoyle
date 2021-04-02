class TextReader():
    def __init__(self, file_path):
        self.file_path = file_path

    def read_text(self):
        raw_data = open(self.file_path, encoding='utf-8').read()
        return raw_data
