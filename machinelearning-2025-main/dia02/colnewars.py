#%%
import pandas as pd
from sklearn import tree
import matplotlib.pyplot as plt
# %%
df = pd.read_parquet("../data/dados_clones.parquet")
# %%
df
#%%
#Nao deveria ter feito a arvore de cara, deveria ter pensado primariamente no problema e realmente visto os dados

features = ['Massa(em kilos)', "Estatura(cm)"]

df.groupby('Status ')[features].mean()
# %%
features = ["Massa(em kilos)","General Jedi encarregado",	
            "Estatura(cm)",
            "Distância Ombro a ombro",	
            "Tamanho do crânio",	
            "Tamanho dos pés",	
            "Tempo de existência(em meses)"]

target = ["Status"]
#PRa tirar os espaços de que tem do nada, assim n me preucupo mais
df.columns = df.columns.str.strip()
# %%
X = df[features]
y = df[target]
#%%
list(df.columns)
#%%
#PRa ver quais tipos estão dentro de uma coluna
X['General Jedi encarregado'].unique()
#%%
X = X.replace({
    'Tipo 1': 1, 'Tipo 2': 2,
    'Tipo 3': 3, 'Tipo 4': 4,
    'Tipo 5': 5,
    'Yoda': 1, 'Shaak Ti': 2, 
    'Obi-Wan Kenobi': 3, 'Aayla Secura': 4, 
    'Mace Windu': 5})

#o proximo passo é retirar os generais pra ver oq ta acontecendo, pra ver se é eles o problema

# %%
model = tree.DecisionTreeClassifier()
model.fit(X=X,y=y)

# %%
plt.figure(dpi=400)
tree.plot_tree(model, feature_names= features,
               class_names= model.classes_,
               filled=True,
               max_depth=3
               )


# %%
