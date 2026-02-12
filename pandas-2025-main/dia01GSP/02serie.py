# %%

idades = [
    32, 38, 50,
    34, 56, 78,
    34, 22, 21,
]

mediaIdade = sum(idades) / len(idades)
print(mediaIdade)

diffs = 0
for i in idades:
    diffs += (i - mediaIdade)**2

variancia = diffs / (len(idades) -1)
print(variancia)
# %%
print(alo alo alo)
# %%

import pandas as pd

series_idades = pd.Series(idades)
varIdade = series_idades.var()
summaryIdade = series_idades.describe()
print(summaryIdade)
# %%
