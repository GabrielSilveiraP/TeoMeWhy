# %%

import pandas as pd
# %%

clientes = pd.read_csv("../data/clientes.csv", sep = ";")
clientes.head()

# %%
filtro = clientes["qtdePontos"] == 0
clientes_0 = clientes[filtro]
#Essa nova coluna abaixo não está em clientes, pois eu criei dentro de um filtro.
clientes_0["flag_1"] = 1
# %%
clientes
# %%
