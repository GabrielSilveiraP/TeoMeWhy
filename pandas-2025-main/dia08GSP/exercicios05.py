#%%
import pandas as pd
# %%
df = pd.read_csv("../data/homicidios.csv", sep = ";")

#%%
df_geral = df.rename(columns = {"valor": "homicideos"})
df_geral.head()
#%%
df_negros = pd.read_csv("../data/homicidios-negros.csv", sep = ";")
df_negros = df_negros.rename(columns = {"valor": "homicideos.negros"})
df_negros.head()
#%%

df_geral.set_index(["nome", "período"])
df_negros.set_index(["nome", "período"])

#%%
pd.concat([df_geral, df_negros], axis = 1)
