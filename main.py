import pandas as pd
import random

dataframe = pd.read_excel('spreadsheets/setor_economico_ajustado.xlsx')

for index, value in enumerate(dataframe['VL_PGTO']):
    if value < 10000 or value / 1e15 >= 1:
        dataframe.at[index, 'VL_PGTO'] = round(random.uniform(10000, 80000), 2)
        
dataframe.to_excel('spreadsheets/setor_economico_ajustado2.xlsx', index=False)
