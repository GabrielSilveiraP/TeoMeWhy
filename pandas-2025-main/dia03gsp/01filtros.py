# %%

import pandas as pd
# %%

df = pd.read_csv("../data/transacoes.csv", sep = ";")
# %%
df.head(5)
# %%
pontos = [1,4,5,7,80,55,90,90]

valores_50_mais = 0
for i in pontos:
    if i >= 50:
        valores_50_mais += 1
valores_50_mais
#Ou teria como fazer mais simplificado porem complexo

# valores_50_mais = [i for i in pontos if i >= 50 ]
# valores_50_mais
# %%

pontos = [1,4,5,7,80,55,90,90]
filtro = []
valores_50_mais = []
for i in pontos:
    filtro.append(i>=50)


resultado = []
for i in range(len(pontos)):
    if filtro[i]:
        resultado.append(pontos[i])
resultado

# %%

brinquedo = pd.DataFrame(
    {
        "nome": ["teo", "nah", "vaiola", "jinx"],
        "idade": [50, 100, 30, 80],
        "uf": ["sp", "pr", "sc", "rj"]
    }
)
brinquedo
# %%
#É uma série, que dentro dela tem um conjunto de booleanos
#Esse numero que usamos é quase o conceito de filtro, mas ele é chamado de escalar porq ele quem vai ser a regua do V ou F
filtro = brinquedo["idade"] >=80
brinquedo[filtro] #Dessa forma só voltou aqueles que deram True.
# %%
filtro_fodase =[False,True]
brinquedo[filtro_fodase]
#Isso não roda por causa que os tamanhos não são correspondentes.
# %%

df = pd.read_csv("../data/transacoes.csv", sep = ";")
df.head(5)

# %%
#Valores maiores que 50
filtroPontos =df["QtdePontos"] >=50
df[filtroPontos]
# %%
#Valores maiores que 50 e menores que 100
#Pandas não tem o operador And, between funciona de outra forma. Mas tem como utilizando o &.
filtroPontos = (df["QtdePontos"] >= 50) & (df["QtdePontos"] < 100)
df[filtroPontos]
#O & pode ser trocado pelo *, por segue o principio da multiplicação de True and False.
# %%
#Iguais a 1 e menores que 100
filtroPontos = (df["QtdePontos"] == 1 ) | (df["QtdePontos"] == 100 )
df[filtroPontos] 

# %%
#Pontos entre 0 e menores que 50 ou do ano de 2025 p frente
filtro = (df["QtdePontos"] > 0) & (df["QtdePontos"] <=50) & (df["DtCriacao"] >= "2025-01-01")
df[filtro]
# %%
