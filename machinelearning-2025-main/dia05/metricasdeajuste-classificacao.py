#%%
import pandas as pd
from sklearn import tree
import matplotlib.pyplot
# %%
df = pd.read_csv("../data/Dados Comunidade (respostas) - dados.csv")
# %%
df = df.replace({"Sim":1, "Não":0})
# %%
df
# %%
#Pega uma coluna que tme variaveis e separa em várias dividindo pelas variáveis, ou seja, vai ter vaárias colunas parecidas e oq muda é se ela é true pro titulo

num_vars = [
    "Curte games?",
    "Curte futebol?",
    "Curte livros?",
    "Curte jogos de tabuleiro?",
    "Curte jogos de fórmula 1?",
    "Curte jogos de MMA?",
    "Idade"]
dummy_vars= [
    "Como conheceu o Téo Me Why?",
    "Quantos cursos acompanhou do Téo Me Why?",
    "Estado que mora atualmente",
    "Área de Formação",
    "Tempo que atua na área de dados",
    "Posição da cadeira (senioridade)"]
# %%
#ali em cima somente pegamos as variaveis para facilitar
df_analise = pd.get_dummies(df[dummy_vars]).astype(int)

df_analise[num_vars] = df[num_vars].copy()

#%%
df_analise['pessoa feliz'] = df['Você se considera uma pessoa feliz?'].copy()
df_analise
#%%
#tem que fazer isso se não a seguinte da problema, por conta da ultima coluna da felicidade lá
features = df_analise.columns[:-1].tolist()
features
# %%
#Vamos montar a arvore agora
X = df_analise[features]
y = df_analise['pessoa feliz'] #variavel resposta
arvore = tree.DecisionTreeClassifier(random_state=42,
                                     min_samples_leaf=5,
                                     )
arvore.fit(X,y)
# %%
arvore_predict = arvore.predict(X)
arvore_predict

# %%
#Pessoa feliz é se a p[essoa reamente é feliz e o predict é oq a arvore predict que é
df_predict = df_analise[['pessoa feliz']]
df_predict['predict_arvore'] = arvore_predict
df_predict
# %%
#o meu deu 1.o o do Teo deu 87. Entao vale a pena fazer os passos seguintes.
#Famosa acurácia, do todo, não dfiz aonde tamo errando
(df_predict['pessoa feliz'] == df_predict['predict_arvore']).mean()

# %%
#matriz de confusão, quantidade de acerto geral

pd.crosstab(df_predict['pessoa feliz'], df_predict['predict_arvore'])
# %%
#os dois batem
(df_predict["pessoa feliz"] ==0).sum()
(df_predict["pessoa feliz"] ==1).sum()
# %%
