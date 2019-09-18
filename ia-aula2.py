# IA

#Importando o módulo de Regressão Linear do scikit-learn
from sklearn.linear_model import LinearRegression

#Preparando dados de treino
# Vamos chamar de X os dados de diâmetro da Pizza.
x = [[7], [10], [15], [30], [45]]

# Vamos chamar de Y os dados de preço da Pizza.
y = [[8], [11], [16], [38.5], [52]]

# Criando o modelo
modelo = LinearRegression()
type(modelo)

# Treinando o modelo
modelo.fit(x, y)

#coeficientes
print('Coeficiente: \n', modelo.coef_)

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


