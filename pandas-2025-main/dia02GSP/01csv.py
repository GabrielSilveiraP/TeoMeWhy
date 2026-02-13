# %%

import pandas as pd

# %%
#df = pd.read_csv("../data/clientes.csv"), dessa forma o pandas nao entende, por causa da diferença entre as linguas (PTbr e EN)
df = pd.read_csv("../data/clientes.csv", sep = ";")
df
# %%

df.to_csv("clientes.csv", index = False) #pra não salvar o indice no dataframe

# %%

df.to_parquet("clientes.parquet", index = False)

# %%

df2 = pd.read_parquet("clientes.parquet")
df2
# %%

df.to_excel("clientes.xlsx", index = False)

df = pd.read_excel("clientes.xlsx")
df
# %%
