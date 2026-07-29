#%%

import pandas as pd

#%%
df = pd.read_csv("homicideos_consolidados.csv", sep = ";")
df.head()

#%%


df = df.set_index(["nome", "período"])
#%%
df_stack = df.stack()
# %%
type(df_stack)

#%%
#se quiser resetar os index
df_stack = df.stack().reset_index()
#%%
df_stack.columns= ["nome", 'período', "metrica", "valor"]

#%%
df_stack.head()

#%%

#Voltou a ser como era antes, mas com duplo indice
(df_stack.set_index(["nome", "período", "metrica"])
        .unstack()
        .reset_index()
)

#%%

df_unstack = (df_stack.set_index(["nome", "período", "metrica"])
        .unstack()
        .reset_index()
)
df_unstack.columns
#%%
metricas = df_unstack.columns.droplevel(0).tolist()[2:1]

df_unstack.columns = [ "nome", "periodo"] + metricas

df_unstack