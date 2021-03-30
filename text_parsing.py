import random
import pandas as pd

class TextParser():
    def __init__(self, file_text):
        self.hidden_text = file_text

    def get_text(self):
        return self.hidden_text

    def set_text(self, file_text):
        self.hidden_text = file_text

    text = property(get_text, set_text)

    def parse_tsv_data(self):
        parsed_data = self.text.replace('\t', '\n').split('\n')

        question_list = parsed_data[0::2]      #retrieving every even index (0, 2, 4, ..)
        answer_list = parsed_data[1::2]        #retrieving every odd index (1, 3, 5, ..)

        qna_df = pd.DataFrame({
            'question': question_list,
            'answer': answer_list
        })

        rand_n = random.randrange(0, len(qna_df['answer']))
        print(qna_df['answer'][rand_n])
