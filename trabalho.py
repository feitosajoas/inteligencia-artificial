# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 19:12:40 2019

@author: joasm
"""

# Realizando import do pandas
import pandas as pd

# Configurando o parâmetro sep=' ', para considerar o espaço como critério de separação das colunas
data = pd.read_csv('C:/Users/joasm/OneDrive/Documentos/trabalhoroque/OVS/features/longIn_m_0.025_i_20.0.csv', sep=' ')
pd.set_option('display.max_columns', None)
print(data.shape)
data.head()

data.info()

data.describe()

#Verificando o farmato dos dados
data.shape

#Verificando as primeiras linhas do dataset
data.head(5)

# Verificando as ultimas linhas do dataset
data.tail(5)

#Verificando se existem valores nulos
data.isnull().values.any()

#Identificando a correlação entre as variáveis
#Correlação não implica causalidade
def plot_corr(data, size = 10):
    corr = data.corr()
    fig, ax = plt.subplots(figsize = (size, size))
    ax.matshow(corr)
    plt.xticks(range(len(corr.columns)), corr.columns)
    plt.yticks(range(len(corr.columns)), corr.columns)
    
#Criando o gráfico
plot_corr(data)

#Visualizando a correlação em tabela
#Coeficiente de correlação:
# +1 = forte correlação positiva
# 0 = não há correlação
# -1 = forte correlação negativa
data.corr()


#Definindo as classes
feature_cols = ['lastTS', 'numPackets', 'totalBytes']
x = data[feature_cols]
y = data.avgInterAT

from sklearn.model_selection import train_test_split

#seleção de variáveis preditoras (Future Selection)
atributos = ['lastTS', 'numPackets', 'totalBytes']

#Variável a ser prevista
atrib_prev = ['feature_cols']

#Importando o módulo de Regressão Linear do scikit-learn
from sklearn.linear_model import LinearRegression

# Criando o modelo
modelo = LinearRegression()
type(modelo)

# Treinando o modelo
modelo.fit(x, y)

#coeficientes
print('Coeficiente: \n', modelo.coef_)

import numpy as np
#MSE (mean square error)
print ("MSE: %.2f" % np.mean((modelo.predict(x) - y) ** 2))

# Score de variação: 1 representa predição perfeita
print('Score de variação: %.2f' % modelo.score(x,y))

# Scatter Plot representando a regressão linear
plt.scatter(x, y, color = 'black')
plt.plot(x, modelo.predict(x))
plt.xlabel('x')
plt.ylabel('y')
plt.xticks(())
plt.yticks(())

# Separando o conjunto de dados entre treino e teste
from sklearn.model_selection import train_test_split
x_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

linreg = LinearRegression()
# Ajsutando o modelo (Aprendendo os coeficientes)
linreg.fit(x_train, y_train)

# Fazendo predições no conjunto de teste
y_pred = linreg.predict(X_test)

#Visualizando a interseção e os coeficientes 
print(linreg.intercept_)
print(linreg.coef_)

#Atributos e seus coeficientes
list(zip(feature_cols, linreg.coef_))

#Fazendo predições no conjunto de teste
y_pred = linreg.predict(X_test)
y_pred

# Calculando MAE utilizando scikit-learn
from sklearn import metrics
print(metrics.mean_absolute_error(y_test,y_pred))

# Calculando MSE utilizando scikit-learn
print(metrics.mean_squared_error(y_test,y_pred))

# Calculando RMSE utilizando scikit-learn
# Importando numpy
import numpy as np
print(np.sqrt(metrics.mean_squared_error(y_test,y_pred)))

#plotando os gráficos de erro
import matplotlib.pyplot

#Plot grafico 1
matplotlib.pyplot.plot(y_test, y_pred)

#Plot grafico 2
matplotlib.pyplot.plot(X_test, y_pred)




