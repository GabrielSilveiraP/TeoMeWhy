#%%
import pandas as pd
from sklearn import linear_model
from sklearn import tree
import matplotlib.pyplot as plt 

#%%
df = pd.read_excel("../data/dados_cerveja_nota.xlsx")
# %%
df.head(10)
# %%

X =df[["cerveja"]] #matriz (dataframe)

y =df[["nota"]] #vetor (séries)
# %%
#X é sempre uma matriz e maiusculo - vetor bidimensional - matriz colunar, e y acaba sendo 
y
# %%
#Qual modelos vamos escolher?
#reg de regressão
#ESSSe é o tal do aprendizado de máquina
reg = linear_model.LinearRegression()
#PRa ajustar o modelo tem que utilizar esse abaixo
reg.fit(X,y.values.ravel())
# %%
reg.coef_
#%%
a, b = reg.intercept_, reg.coef_[0]
print(a,b)
 # %%
#Não esquece o ()
predict_reg = reg.predict(X.drop_duplicates())
predict_reg
# %%

plt.plot(X['cerveja'], y, 'o')
plt.grid(True)
plt.title("Relação de cerveja VS Nota")
plt.xlabel("Cerveja")
plt.ylabel("Nota")
plt.plot(X.drop_duplicates()['cerveja'], predict_reg)
#tem que rodar tudo numa mesma célula
plt.legend(["Observado", f'y= {a:.2f}+ {b:.2f} x'])
# %%
#TUDO ISSO ACIMA foi de regressão, agora a baixo é da árvore
# %%
#arvore full
arvore_full = tree.DecisionTreeRegressor(random_state=42)

arvore_full.fit(X,y)

predict_arvore_full = arvore_full.predict(X.drop_duplicates())

arvore_d2 = tree.DecisionTreeRegressor(random_state=42, max_depth=2)

arvore_d2.fit(X,y)

predict_arvore_d2 = arvore_d2.predict(X.drop_duplicates())
# %%
plt.plot(X['cerveja'], y, 'o')
plt.grid(True)
plt.title("Relação de cerveja VS Nota")
plt.xlabel("Cerveja")
plt.ylabel("Nota")
plt.plot(X.drop_duplicates()['cerveja'], predict_reg)
plt.plot(X.drop_duplicates()["cerveja"], predict_arvore_full)
plt.plot(X.drop_duplicates()["cerveja"], predict_arvore_d2)

plt.legend(["Observado", 
            f'y= {a:.2f}+ {b:.2f} x',
            'Árvore Full',
            'Árvore Depth = 2'
            ])
# %%
#A mudança da full p d2 é que uma é uma overfittada e a d2 tem uma profundida diminuida, da pra ver que ela não é tão abrupta quanto a full.
#Max_depth= é no máximo 2 quebras, gerando 4 nós e portanto 4 médias. É um pouco confuso, mas pense assim, no primeiro nivel tem somente um grupo uma média ->splitou, 2 grupos-> agora tem 2 caixas 2 médias-> splitou dnv-> agr tem 4 grupos, 4 médias. p uma arvore simetrica claro, e o max força essa parada

#%%
#Oq eu falei ali em cima mostra aqui embaixo
plt.figure(dpi = 500)

tree.plot_tree(arvore_d2,
               feature_names=['cerveja'],
               filled= True)
# %%
