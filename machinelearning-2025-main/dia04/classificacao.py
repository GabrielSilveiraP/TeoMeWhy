#%%
import pandas as pd
import matplotlib.pyplot as plt

from sklearn import linear_model
from sklearn import tree
from sklearn import naive_bayes

# %%
df = pd.read_excel("../data/dados_cerveja_nota.xlsx")
# %%
df 
#criar uma classe dos aprovados -> astype pra transformar em binário, porq era true e false antes
#%%
df["aprovados"] = (df["nota"] > 5).astype(int)
# %%
plt.plot(df["cerveja"], df["aprovados"], 'o', color = "royalblue")
plt.grid(True)
plt.title("Cerveja x Aprovação")
plt.xlabel("Cervejas")
plt.ylabel("Aprovados")
# %%
#reg de regressão
reg = linear_model.LogisticRegression(penalty=None, fit_intercept=True)
# %%
#O fit exige que X seja 2D, no formato (n_amostras, n_features), porque o sklearn foi feito para aceitar várias features. df["cerveja"] devolve uma Series 1D (erro), enquanto df[["cerveja"]] devolve um DataFrame (n, 1), que é o formato esperado.
reg.fit(df[["cerveja"]], df["aprovados"])
# %%
reg_predict = reg.predict(df[["cerveja"]].drop_duplicates())
reg_proba = reg.predict_proba(df[["cerveja"]].drop_duplicates())[:,1]
#abaixo tem as coisas da arvore
arvore_full = tree.DecisionTreeClassifier(random_state=42)
arvore_full.fit(df[["cerveja"]], df["aprovados"])
arvore_full_predict = arvore_full.predict(df[["cerveja"]].drop_duplicates())
arvore_full_proba = arvore_full.predict_proba(df[["cerveja"]].drop_duplicates())[:,1]

nb = naive_bayes.GaussianNB()
nb.fit(df[["cerveja"]], df["aprovados"])
nb_predict = nb.predict(df[["cerveja"]].drop_duplicates())
nb_predict_proba = nb.predict_proba(df[["cerveja"]].drop_duplicates())[:,1]
# %%
reg_predict
# %%
plt.plot(df["cerveja"], df["aprovados"], 'o', color = "royalblue")
#Tem importancia a ordem desses dois plotados
plt.plot(df["cerveja"].drop_duplicates(),reg_predict, color = "tomato")
plt.grid(True)
plt.title("Cerveja x Aprovação")
plt.xlabel("Cervejas")
plt.ylabel("Aprovados")

# plt.plot(df["cerveja"].drop_duplicates(),arvore_full_predict, color = "green")
# plt.plot(df["cerveja"].drop_duplicates(),arvore_full_proba, color = "magenta")

plt.plot(df["cerveja"].drop_duplicates(),nb_predict, color = "green")
plt.plot(df["cerveja"].drop_duplicates(),nb_predict_proba, color = "magenta")

plt.hlines(0.5,xmin=1,xmax=9,linestyles="--", colors= "black")
#aqui embaixo tem o valor da regressão logistica, porq ela é uma curva 
plt.plot(df["cerveja"].drop_duplicates(),reg_proba, color = "red")
plt.legend(["Observação", 
            "Reg Predict", 
            "Reg Proba",
            "Naive BayesPredict",
            "Naive Bayes Proba",
            ])


# %%
plt.plot(df["cerveja"].drop_duplicates(),reg_predict, color = "tomato")
plt.grid(True)
plt.title("Cerveja x Aprovação")
plt.xlabel("Cervejas")
plt.ylabel("Aprovados")

plt.plot(df["cerveja"].drop_duplicates(),nb_predict, color = "green")
plt.plot(df["cerveja"].drop_duplicates(),nb_predict_proba, color = "magenta")

plt.hlines(0.5,xmin=1,xmax=9,linestyles="--", colors= "black")
#aqui embaixo tem o valor da regressão logistica, porq ela é uma curva 
plt.plot(df["cerveja"].drop_duplicates(),reg_proba, color = "red")
plt.legend(["Observação", 
            "Reg Predict", 
            "Reg Proba",
            "Árvore Full Predict",
            "Árvore Full Proba",
            ])