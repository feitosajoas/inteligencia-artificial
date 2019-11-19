# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 20:48:55 2019

@author: Aluno
"""

from IPython.display import Image
Image('ConfusionMatrix.jpg')

#Criando uma Confusion Matrix
print("Confusuin Matrix")

print("{0}".format(metrics.confunsion_matrix(Y_teste, nb_predict_test, labels = [1, 0])))
print("")

print("Classification Report")
print(metrics.classification_report(Y_teste, nb_predict_test, labels = [1, 0]))

