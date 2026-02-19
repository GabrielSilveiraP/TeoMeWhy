# %%

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %%

clientes = pd.read_csv("../data/clientes.csv", sep = ";")

clientes
# %%

clientes["qtdePontos"].sort_values()

# %%
#Qual é a maior qtd de ponto
clientes["qtdePontos"].max()
# %%
#Dessa forma consigo enxergar quem são os maiores pontuadores 
clientes.sort_values(by = "qtdePontos", ascending = False)
# %%
#Ele retorna um dataframe novo, não uma view - como um filtro que vimos-
clientes.sort_values(by = "qtdePontos", ascending = False).head(5)
# %%
#Agora temos quem são os 5 primeiro por causa que interligamos os pontuadores e mandei mostrar só o id deles
(clientes.sort_values(by = "qtdePontos", ascending = False)
            .head(5)["idCliente"])
# %%

brinquedo = pd.DataFrame(
    {
        "nome": ["teo", "ana", "maria", "josé"],
        "salario":["1000", "3000", "3000", "1500"],
        "idade":["18", "20", "25", "87"],
    }
)

brinquedo
# %%
#Aq ele ordena pelo salário e depois pela iddade
brinquedo.sort_values(by=["salario", "idade"], ascending = False)
# %%
#Agora eu tenho as caracteristicas do bglh de cima s'que com cada criterio de sort tendo uma organizaçao diferente
brinquedo.sort_values(by=["salario", "idade"], ascending = [False, True])
# %%
