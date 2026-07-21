# %%
import pandas as pd

# %%

idades = [23,56,78,98,34,65,74,13,56,23]

idades = pd.Series(idades)
# %%

idades.sum()
idades.min()
idades.mean()
idades.describe()
#%%
#esse describe da uma métricas 
#%%
idades.max()
# %%

clientes = pd.read_csv("../data/clientes.csv", sep = ";")
clientes
# %%
clientes["flTwitch"].sum()
#%%
clientes["flTwitch"].mean()
#%%
RedesSociais = ["flEmail","flTwitch","flYouTube","flBlueSky","flInstagram"]
#%%
#Shift (Seleciona oq ta em comum) -> Ctrl + d (encontra os outros iguais nas palavras da frente) ->Ctrl+Shift (na palavratoda) -> Aq afz o comando q quiser, ali em cima por exemplo adicionei as aspas
# %%
clientes[RedesSociais].mean
# %%
#pra puxar aqueles que sejam string
filtro = clientes.dtypes == "object"
#%%
clientes.dtypes[filtro]
#%%
#aq eu to negando o filtro, tudo q é ao contrario de object
clientes.dtypes[~filtro].index .tolist()
# %%
#Puxar somente aqueles q n sejam
num_columns = clientes.dtypes[~(clientes.dtypes == "object")].index.tolist()
#%%
clientes[num_columns].mean()
# %%
clientes[num_columns].describe()
# %%
    