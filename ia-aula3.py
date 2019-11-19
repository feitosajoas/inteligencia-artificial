# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 19:39:00 2019

@author: Aluno
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#Carregando o dataset
df = pd.read_csv("pima-data.csv")

#Verificando o farmato dos dados
df.shape

#Verificando as primeiras linhas do dataset
df.head(5)

# Verificando as ultimas linhas do dataset
df.tail(5)

#Verificando se existem valores nulos
df.isnull().values.any()

#Identificando a correlação entre as variáveis
#Correlação não implica causalidade
def plot_corr(df, size = 10):
    corr = df.corr()
    fig, ax = plt.subplots(figsize = (size, size))
    ax.matshow(corr)
    plt.xticks(range(len(corr.columns)), corr.columns)
    plt.yticks(range(len(corr.columns)), corr.columns)
    
#Criando o gráfico
plot_corr(df)

#Visualizando a correlação em tabela
#Coeficiente de correlação:
# +1 = forte correlação positiva
# 0 = não há correlação
# -1 = forte correlação negativa
df.corr()

#Definindo as classes
diabetes_map = {True : 1, False : 0}

#Aplicando o mapeamento ao dataset
df['diabetes'] = df['diabetes'].map(diabetes_map)

#Verificando as primeiras linhas do dataset
df.head(5)

#Verificando como os dados estão distribuídos
num_true = len (df.loc[df['diabetes'] == True])
num_false = len (df.loc[df['diabetes'] == False])
print("Número de casos verdadeiros: {0} ({1:2.2f}%)".format(num_true, (num_true/ (num_true + num_false)) * 100))
print("Número de casos falsos: {0} ({1:2.2f}%)".format(num_false, (num_false/ (num_true + num_false)) * 100))


