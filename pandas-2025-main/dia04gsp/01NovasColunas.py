# %%

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %%
df = pd.read_csv("../data/clientes.csv", sep = ";")
df.sample(5)

# %%
#Essa é a maneira lógica dentro do pandas de somar coisas em colunas
df["qtdePontos"] + 100
# %%
#Agora, se estivessemos no python puro teriamos q fazer um for ou while(elementos de repetição)
nova_coluna = []
for i in df["qtdePontos"]:
    nova_coluna.append(1+100)

nova_coluna
#Como foi descrito acima, mas lembre-se que conhecer a biblioteca é essencial por poupa linha e tempo. 
#Motivos pra NAO fazer esse: precisa acessar elemento a elemento, fazer append de listas é custoso, nao é uma operacao direta.
# %%
#Criando uma coluna nova dentro do df
df["Pontos+100"] = df["qtdePontos"] + 100
df
# %%

df["SomaEmailTwich"] = df["flEmail"] + df["flTwitch"]
df
# %%
filtro = df["SomaEmailTwich"] > 0
filtro

# %%
df["QtdRedesSociais"] = df["flEmail"] +	df["flTwitch"] +	df["flYouTube"] + df["flBlueSky"] + df["flInstagram"]
df
# %%
#Quem que tem todas as redes sociais
df["TodasSociais"] = df["flEmail"] *	df["flTwitch"] * df["flYouTube"] * df["flBlueSky"] * df["flInstagram"]
df
# %%
df["qtdePontos"].describe()
# %%
#O numyp funciona para questões matematicas, coseno, seno, log, coisarada e ele é muito rápido
df["logPontos"] = np.log(df["qtdePontos"]+1)
#Esse +1 é para evitar que de -inf, por tem vezes q pode ter 0 e log de 0 é -infinito
# %%
df["logPontos"].describe()

# %%
plt.hist(df["logPontos"])
plt.grid(True)
plt.show()
# %%
