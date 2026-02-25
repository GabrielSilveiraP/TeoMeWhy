# %%

import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep = ";")
clientes
# %%
#Limpando o NaN, lembre-se que aqui eu to criando uma view, preciso reatribui
clientes.dropna(inplace = True)
#O default é ele apagar a linha inteira se tiver um Nan, mas da para modificar isso.
clientes.dropna(how="any") #-> default
clientes.dropna(how="all")
#Dessa forma ele só vaia apagar se a linha inteira estiver em Na
# %%

df = pd.DataFrame(
    {   
        "nome": ["teo", None, "eduarda", "camila"],
        "idade": [None, None, 35, 40],
        "salário": [1000, 2000, None, 1245]
    }
)
df.dropna(how="all")
# %%
df.dropna(how="all",subset=["nome", "idade"])
# %%
#É literalmente um replace do Na, onde vai trocar tudo q for Na por 0 ou qualquer valor -substitui a célula-
df["idade"].fillna(0)

# %%
#Tem até como mudar mais de uma linha ao mesmo tempo
df.fillna({"nome": "desconhecido", "idade": 0})
# %%
médiasSubstuicao = df[["idade", "salário"]].mean()
df.fillna(médiasSubstuicao)
# %%
