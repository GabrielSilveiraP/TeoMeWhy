#%%
import pandas as pd
from sklearn import tree
import matplotlib.pyplot as plt
#%%
df = pd.read_excel("../data/dados_cerveja.xlsx")

df.head()
# %%
features = [ "temperatura","copo","espuma","cor"]
target = "classe"

X = df[features]
y = df[target]
#Lembra de fazer X= X replace, se fizer somente x.replace, como é uma mascara, não vai ser o df puxado, ele vai puxar o X original
X = X.replace({
    'mud': 1, 'pint': 2,
    'sim': 1, 'não': 0,
    'clara': 0, 'escura': 1,
})
# %%# deu errado aqui por conta de ter texto no meio do df, por isso rolou a conversão aqui em cima
#model.fit(X=X, y=y)
# %%
#Oque é o modelo? Existe vários, precisam servir para nós, tem que ajustar o modelo para que funcione em mais de uma coisa. Uma camiseta de modelo M serve em mais de uma pessoa, agora uma alfaiataria não
model = tree.DecisionTreeClassifier()
model.fit(X=X,y=y)

# %%
plt.figure(dpi=400)
tree.plot_tree(model, feature_names= features,
               class_names= model.classes_,
               filled=True
               )

