# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 20:34:17 2019

@author: Aluno
"""

from sklearn import metrics

nb_predict_train = modelo_vl.predict(X_treino)

print("Exatidão (Accuracy): {0:4f}".format(metrics.accuracy_score(Y_treino, nb_predict_train)))
print()

#Verificando a exatidão do modelo de dados de teste
nb_predict_test = modelo_vl.predict(X_teste)

print("Exatidão (Accuracy): {0:4f}".format(metrics.accuracy_score(Y_teste, nb_predict_train)))
print()