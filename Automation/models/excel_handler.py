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
    
    def get_table_data(self):
        # Columns to be include
        columns_to_include = [col for col in self.df.columns if col != 'Obs']
    
        # Create dict
        data = self.df[columns_to_include].dropna(how='all').to_dict(orient='records')
    
        return data

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

    def mark_failure(self, item: dict):
        name = item.get('Produto')
        index = self.df[self.df.iloc[:, 0] == name].index
        if not index.empty:
            i = index[0]
            self.df.at[i, 'Status_Processamento'] = 'Failure'

            current_obs = str(self.df.at[i, 'Obs']).strip()
            new_message = "Can't be added on TN5250J"
            if new_message not in current_obs:
                if current_obs:
                    updated_obs = f"{current_obs}; {new_message}"
                else:
                    updated_obs = new_message
                self.df.at[i, 'Obs'] = updated_obs
