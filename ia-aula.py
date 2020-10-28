# IA

import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline

#diâmetro (cm)
diametros = [[7], [10], [15], [30], [45]]

#preços 
precos = [[8], [11], [16], [38.5], [52]]

#métodos de figura e cálculos
plt.figure()
plt.xlabel('Diâmetros(ccm)')
plt.ylabel('Preços(R$)')
plt.title('Diâmetro x Preço')
plt.plot(diametros, precos, 'k.')
plt.axis([0, 60, 0, 60])
plt.grid(True)
plt.show()
