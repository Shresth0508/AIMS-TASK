import pandas as pd

class SimpleImputer:
    def __init__(self, data):
        self.data = data
        self.columns_with_missing_values = []

    def identify_columns_with_missing_values(self):
        for column in self.data.columns:
            if self.data[column].isnull().sum() > 0:
                self.columns_with_missing_values.append(column)

    def impute_missing_values(self, strategy):
        for column in self.columns_with_missing_values:
            if self.data[column].dtype != "object":
                if strategy.lower() == "mean":
                    mean_value = self.data[column][self.data[column] != 'NA'].astype(float).mean()
                    self.data[column].fillna(mean_value, inplace=True)

                elif strategy.lower() == "median":
                    median_value = self.data[column][self.data[column] != 'NA'].astype(float).median()
                    self.data[column].fillna(median_value, inplace=True)

                elif strategy.lower() == "mode":
                    mode_value = self.data[column][self.data[column] != 'NA'].astype(float).mode().iloc[0]
                    self.data[column].fillna(mode_value, inplace=True)

            elif self.data[column].dtype == "object":
                mode_value = self.data[column].mode().iloc[0]
                self.data[column].fillna(mode_value, inplace=True)

    def get_imputed_data(self):
        return self.data


class CustomOneHotEncoder:
    def __init__(self, data):
        self.data = data

    def one_hot_encode_column(self, column):
        one_hot_df = pd.get_dummies(self.data[column], prefix="", prefix_sep="")
        self.data = pd.concat([self.data, one_hot_df], axis=1)
        self.data = self.data.drop(column, axis=1)

    def one_hot_encode_all_columns(self):
        for column in self.data.columns:
            if self.data[column].dtype == "object":
                self.one_hot_encode_column(column)

    def get_encoded_data(self):
        return self.data


if __name__ == "__main__":
    file_path = '/Users/SHRESTH/Downloads/TEST.csv'
    data = pd.read_csv(file_path)

    # Impute missing values
    imputer = SimpleImputer(data)
    imputer.identify_columns_with_missing_values()
    imputer.impute_missing_values("mean")
    imputed_data = imputer.get_imputed_data()

    print(imputed_data)

    # One-hot encode columns
    encoder = CustomOneHotEncoder(imputed_data)
    encoder.one_hot_encode_all_columns()
    encoded_data = encoder.get_encoded_data()

    print(encoded_data.astype('int'))