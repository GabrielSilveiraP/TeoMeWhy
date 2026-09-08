#%%
import pandas as pd
from sklearn import tree
import matplotlib.pyplot as plt
#%%
df = pd.read_excel("data/dados_frutas.xlsx")
# %%
df
# %%
arvore = tree.DecisionTreeClassifier(random_state=42)
# %%
 y = df["Fruta"]
#%%
caracteristicas = [ "Arredondada", "Suculenta", "Vermelha", "Doce"]



# %%
#lembrar de não colocar o "" aqui pois não é uma coluna q existe
#esse x agrupa so as caracteristicas, remove a fruta no final
x = df[caracteristicas]


# %%
x
y
# %%
#isso tem q se atentar porq se não tiver certo da problema, tem que ser o mesmo tamanho de x e y tbm. Daqui pra frente é o LEARNING do machine
arvore.fit(x, y)

# %%
arvore.predict([[0,1,0,0]])
#Limão não é suculenteo kkkkkk
# %%
arvore.predict([[0,0,0,0]])
# %%
#agora para desenhar a arvore que fizemos
# %%
#Importante o .unique para que seja contagem distinta
plt.figure(dpi=500)
tree.plot_tree(arvore, 
               feature_names= caracteristicas,
                class_names=arvore.classes_,
                 filled=True )
#Doido até que a Maçã não aparece no plot
# %%
probabilidade = arvore.predict_proba([[1,1,1,1]])[0]
pd.Series(probabilidade, index = arvore.classes_)
#Ta calculando a probabilidade de ser oq eu to pedindo, ou seja, se for 1 1 1 1, seja arredondada, suculentea etc. E nesse caso da 50% de chance de ser Cereja e 50% Maçã
# %%
