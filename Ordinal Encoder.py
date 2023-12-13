import pandas as pd

class OrdinalEncoder:
    def __init__(self, data):
        self.data = data
        self.val = 0
        self.key_exhausted = {}

    def encode_column(self, column):
        if self.data[column].dtype == "object":
            for i in self.data[column]:
                if i not in self.key_exhausted:
                    self.data[column] = self.data[column].replace(i, self.val)
                    self.val += 1
                    self.key_exhausted[i] = True

    def encode_all_columns(self):
        for column in self.data.columns:
            self.encode_column(column)
            self.val=0
            self.key_exhausted = {}

    def get_encoded_data(self):
        return self.data

if __name__ == "__main__":
    file_path = '/Users/SHRESTH/Downloads/TEST.csv'
    data = pd.read_csv(file_path)

    encoder = OrdinalEncoder(data)
    encoder.encode_all_columns()

    encoded_data = encoder.get_encoded_data()
    print(encoded_data)