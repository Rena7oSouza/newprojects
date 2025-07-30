import pandas as pd

class ExcelHandler:
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.df = pd.read_excel(filepath)
        
        # Ensure required columns exist
        for column in ['Valor', 'Descrição', 'Status_Processamento', 'Obs']:
            if column not in self.df.columns:
                self.df[column] = ''

    def get_product_names(self):
        # Return non-empty product names from the first column
        return self.df.iloc[:, 0].dropna().tolist()

    def update_product_data(self, results: list[dict]):
        # Update the dataframe with scraped data
        for result in results:
            name = result['name']
            index = self.df[self.df.iloc[:, 0] == name].index
            if not index.empty:
                i = index[0]
                self.df.at[i, 'Valor'] = result.get('price', '')
                self.df.at[i, 'Descrição'] = result.get('title', '')
                self.df.at[i, 'Status_Processamento'] = result.get('status', '')
                self.df.at[i, 'Obs'] = result.get('obs', '')

        # Save the updated Excel file
        self.df.to_excel(self.filepath, index=False)
