#%%

import pandas as pd
from sklearn import model_selection
from sklearn import tree
import matplotlib.pyplot as plt

df = pd.read_csv("../data/abt_churn.csv")
df.head()
# %%
#SEMMA-> Sample, Explore, Modify, Model and Assess
#%%

df['dtRef'].value_counts().sort_index()
# %%
#Out of time. Filtramo p pegar o oot
oot = df[df['dtRef'] ==df['dtRef'].max()].copy()
oot
# %%
#lembrar q esse é o resto e ainda vmaos separar em treino e teste
df_train = df[df['dtRef']<df['dtRef'].max()].copy()
df_train
# %%
df_train.head()
# %%
#da segunda coluna até a penultima, porq a ultima é a flag churn, que é oq queremos prever
#variaveis
features = df_train.columns[2:-1]
#nossa target
target = 'flagChurn'

X, y = df_train[features], df_train[target]
#%%
#SAMPLE
#Lembrar que o X e o y tem que ser iguais
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y ,
                                                                      random_state = 42,  
                                                                      test_size = 0.2,
                                                                      stratify=y)
#o 0,2 é porq eu to definindo que vai ser 20% da minha base total

#testando para ver se as duas amostras  são parecidas. Antes de estratificar elas eram mais diferentes 
print("Taxa variável respsota:", y_train.mean())
print("Taxa variável resposta:", y_test.mean())
print("Taxa variável resposta:", y.mean())
# %%
#explore missing
X_train.isna().sum().sort_values(ascending = False)
# %%
#analise bivariada
#na primeira vez q rodou tava sem copy aq embaixo, dai deu merda. Porq ele é essencial
df_analise = X_train.copy()
df_analise[target] = y_train
sumario = df_analise.groupby(by=target).agg(["mean", "median"]).T
sumario
# %%
#esse n é muito util vistoq ue podem estar em casas, grandezas diferentes
sumario['dif_aboluta'] = sumario[0] - sumario[1]
sumario
# %%
sumario['dif_relativa'] = sumario[0] / sumario[1]
sumario.sort_values(by = ['dif_relativa'], ascending = False)
# %%
arvore = tree.DecisionTreeClassifier(random_state=42, max_depth=5)
arvore.fit(X_train,y_train)
# %%
#plotando a arvore

plt.figure(dpi=500, figsize=4,4)
tree.plot_tree(arvore, feature_names=X_train.columns, filled=True, class_names=[str(i) for i in arvore.classes_])

# %%
arvore.feature_importances_
# %%
feature_importances = (pd.Series(arvore.feature_importances_, index = X_train.columns).sort_values(ascending = False).reset_index())

feature_importances['acumulada'] = feature_importances[0].cumsum()
feature_importances
# %%
#Pra conseguir buscar todos aqueles que tem pouca influencia e vapo neles
feature_importances[feature_importances['acumulada'] < 0.96]