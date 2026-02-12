# %%

import pandas as pd

idades = [
    32, 38, 50,
    34, 56, 78,
    34, 22, 21,
]
nomes = [
    "ana", "bia", "carlos",
    "daniel", "eduardo", "fernando",
    "gabriel", "hugo", "hugo",
]

series_idades = pd.Series(idades)
series_nomes = pd.Series(nomes)
series_nomes 
# o dataframe pode ser considerado um varal onde penduramos as series nele ou q o dtaframe é um conjunto de series
# %%

df = pd.DataFrame()
df["idades"] = series_idades
df["nomes"] = series_nomes
df
# %%

df.iloc[0] #aq me retornou a primeira linha da minha planilha
df.iloc[0]["nomes"]
df.iloc[-1]["idades"]

# %%

