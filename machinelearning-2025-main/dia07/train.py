#%%

import pandas as pd
import mlflow
from sklearn import model_selection, naive_bayes
from sklearn import tree
from sklearn import linear_model, ensemble
from sklearn import metrics, pipeline
import matplotlib.pyplot as plt
from feature_engine import discretisation, encoding

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

plt.figure(dpi=500, figsize=(4,4))
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
# %%

best_features = (feature_importances[feature_importances['acumulada'] < 0.96]["index"].tolist())
best_features
#%%
# --- CAMINHO B: desativado, passo manual, segue para o (Caminho A) da pipe q eu to usando abaixo ---
# tree_discredization = discretisation.DecisionTreeDiscretiser(
#     variables=best_features,
#     regression=False,
#     bin_output="bin_number",
#     cv=3)
# onehot = encoding.OneHotEncoder(variables=best_features, ignore_format=True)
# reg = linear_model.LogisticRegression(penalty=None, random_state=42, max_iter=1000000)
#
# model_pipeline = pipeline.Pipeline(steps=[
#     ("Discretizar", tree_discredization),
#     ("Onehot", onehot),
#     ("Model", reg)
# ])
# model_pipeline.fit(X_train[best_features], y_train)
#%%
#arvorenova = tree.DecisionTreeClassifier(random_state=42)
#arvorenova.fit(X_train_transform, y_train)
#(pd.Series(arvorenova.feature_importances_, index=X_train_transform.columns).sort_values(ascending=False))
#%%
#As linhas abaixo poderiam ser inseridas abaixo de modify, decidi deixar por aqui para mostrar a diferença dos metodos, um que é mais espaçado e esse q é fazer um pipe
#Ou seja, fazer com que o x_trasnform seja discretizado, onehot e o modelo fitado numa só
# PIPELINE
tree_discretisation = discretisation.DecisionTreeDiscretiser(
    variables=best_features,
    regression=False,
    bin_output='bin_number',
    cv=3,
)
onehot = encoding.OneHotEncoder(variables=best_features, ignore_format=True)
#reg = linear_model.LogisticRegression(penalty=None, random_state=42, max_iter=1000000)
#acima temos regressao e abaixo temos outro modelo, que é o Naive bayes
#model = naive_bayes.BernoulliNB() #não é melhor que o outro modelo
#modelos de ensamble -> random forest é um deles, que soma a probabilidade
#testei todos eses modelos e o melhor foi o rf
model = ensemble.RandomForestClassifier(random_state=42,
                                         n_jobs=2,
                                         )
#model = ensemble.AdaBoostClassifier(random_state=42,
 #                                   n_estimators=500,
#                                    learning_rate=0.99
#                                    )
#Quanto mais perto de 1 o learning rate mais perto de overfita
#Gradient boost olha para os residuos-erros, para reduzir esses ruidos



params = {
        "min_samples_leaf":[15,20,25,30,50],
        "n_estimators" : [100,200,500,1000],
        "criterion" : ["gini", "entropy", "log_loss"],       
}

grid = model_selection.GridSearchCV(model, 
                                    params,
                                    cv=3,
                                    scoring="roc_auc",
                                    verbose=4)

model_pipeline = pipeline.Pipeline(steps=[
    ("Discretizar", tree_discretisation),
    ("Onehot", onehot),
    ("Grid", grid),
])

#mlflow de cria
mlflow.set_tracking_uri("http://127.0.0.1:5000")
mlflow.set_experiment(experiment_name="churn_dos_guri")
with mlflow.start_run(run_name=model.__str__()):
    mlflow.sklearn.autolog()
    model_pipeline.fit(X_train[best_features], y_train)



    #No meu cdoigo eu precisei encirporar o x_trains[best_features] por conta que ele n tava aceitando o X_train_transform
    y_train_predict = grid.predict(X_train[best_features])
    y_train_proba = grid.predict_proba(X_train[best_features])[:, 1]

    acc_train = metrics.accuracy_score(y_train, y_train_predict)
    auc_train = metrics.roc_auc_score(y_train, y_train_proba)
    roc_train = metrics.roc_curve(y_train, y_train_proba)
    print("Acurácia Treino", acc_train)
    print("Auc Treino", auc_train)

    y_test_predict = grid.predict(X_test[best_features])
    y_test_proba = grid.predict_proba(X_test[best_features])[:,1]


    acc_test = metrics.accuracy_score(y_test,y_test_predict)
    auc_test = metrics.roc_auc_score(y_test, y_test_proba)
    roc_test = metrics.roc_curve(y_test, y_test_proba)
    print("Acurácia Teste", acc_test)
    print("Auc Teste", auc_test)
    y_oot_predict = grid.predict(oot[best_features])
    y_oot_proba = grid.predict_proba(oot[best_features])[:,1]


    acc_oot = metrics.accuracy_score(oot[target],y_oot_predict)
    auc_oot = metrics.roc_auc_score(oot[target], y_oot_proba)
    roc_oot = metrics.roc_curve(oot[target], y_oot_proba)
    print("Acurácia oot", acc_oot)
    print("Auc oot", auc_oot)


    mlflow.log_metrics({ 
    "acc_train" :acc_train,
    "acc_test" :    acc_test,
    "auc_test" :    auc_test,
    "auc_train":    auc_train,
    "acc_oot" :    acc_oot,
    "auc_oot" :    auc_oot,

    })
# %%
plt.plot(roc_train[0], roc_train[1])
plt.plot(roc_test[0], roc_test[1])
plt.plot(roc_oot[0], roc_oot[1])
plt.grid(True)
plt.title("Curva ROC")
plt.legend([
    f"Treino: {100*auc_train:.2f}",
    f"Test: {100*auc_test:.2f}",
    f"Out of time: {100*auc_oot:.2f}"
])
# %%
#serialização, binárizar o estado do objeto-> porq dai se movermos ele é ais fácil trazer em python. 

# model_df = pd.Series( {
    
#     "model":model_pipeline,
#     "features": best_features
# })

# model_df.to_pickle("model.pkl")

#pelo meu modelo estar salvo no mlflow n preciso disso, de salvar e dps nem de importar
# %%
