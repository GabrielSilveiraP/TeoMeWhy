# %%
import pandas as pd

idades = [
    32, 38, 50,
    34, 56, 78,
    34, 22, 21,
]

series_idades = pd.Series(idades)
series_idades

# %%
#idades[0] -> o primeiro da lista
#idades[-1] -> o ultimo da lista

# %%

#series_idades[-1] da keyError, erro crucial
series_idades = series_idades.sort_values()
series_idades

# %%
series_idades[0] # o indice fica vinculado ao elento da serie, por mais que tenhamos organizado o 0 continua sendo o 32, e nao o 21.

# %%
series_idades.iloc[0] #agora com ele estamos falando em posição e nao mais em chave
series_idades.iloc[-1] #puxou o 78, que é o ultimo numero da lista ordenada
series_idades.iloc[:3] #os tres primeiros numeros da lista -lembre-se- ordenada, essa bomba se chama slice
series_idades.iloc[::-1] # inverti a lista, agora está do maior para o menor
# %%
idades = [
    32, 38, 50,
    34, 56, 78,
    34, 22, 21,
]
indexs = [
    "ana", "bia", "carlos",
    "daniel", "eduardo", "fernando",
    "gabriel", "hugo", "hugo",
]

series_idades = pd.Series(idades, index = indexs)
series_idades
# %%
 
series_idades["hugo"] #posso puxar pelo nome e ele vai me entregar a idade
series_idades.iloc[[-1]] #assim retorna tanto o nome quanto a idade, meio q a linha inteira do ultimo


# %%
