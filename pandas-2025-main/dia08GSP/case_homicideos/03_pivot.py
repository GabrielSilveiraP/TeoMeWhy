#%%

import pandas as pd

#%%

df = pd.read_csv("homicideos_consolidados.csv", sep = ";")

df.head()

#%%

df_stack = (df.set_index(["nome", "período"])
    .stack()
    .reset_index()
 )

df_stack.columns = ["nome", "periodo", "metricas", "valor"]

#%%

(df_stack.pivot_table(values = "valor", 
                     index = ["nome","periodo"],
                     columns="metricas")
        .reset_index()
)           

#%%
#Nome dos estados e a media do valor dos estados direto na coluna. A dimensao de periodo sumiu, por isso tivemos que botar a agg, dai nela da pra brinca
df_stack.pivot_table(values="valor",
              index=["nome"],
              columns='metricas',
              aggfunc='mean'
              )

#aggfunc='max', aggfunc='min'
#pivot table é contrário de .stack()