

class TextReader():
    def __init__(self, file_path):
        self.hidden_path = file_path

    def get_path(self):
        return self.hidden_path

    def set_path(self, file_path):
        self.hidden_path = file_path

    path = property(get_path, set_path)

    def print_file(self):
        raw_data = open(self.path, encoding='utf-8').read()
        print(raw_data[1:136])
