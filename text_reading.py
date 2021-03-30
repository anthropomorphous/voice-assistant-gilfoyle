class TextReader():
    def __init__(self, file_path):
        self.hidden_path = file_path

    def get_path(self):
        return self.hidden_path

    def set_path(self, file_path):
        self.hidden_path = file_path

    path = property(get_path, set_path)

    def read_text(self):
        raw_data = open(self.path, encoding='utf-8').read()
        return raw_data
