import pandas as pd

class ExcelHandler:
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.df = pd.read_excel(filepath)
        for col in ['Valor', 'Descrição', 'Status_Processamento', 'Obs']:
            if col in self.df.columns:
                self.df[col] = self.df[col].astype(object)

    def get_product_names(self):
        return self.df.iloc[:, 0].dropna().tolist()

    def update_product_data(self, results: list[dict]):
        for result in results:
            name = result['name']
            index = self.df[self.df.iloc[:, 0] == name].index
            if not index.empty:
                i = index[0]
                self.df.at[i, 'Valor'] = result.get('price', '')
                self.df.at[i, 'Descrição'] = result.get('title', '')
                self.df.at[i, 'Status_Processamento'] = result.get('status', '')
                self.df.at[i, 'Obs'] = result.get('obs', '')
        self.df.to_excel(self.filepath, index=False)
