#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Exercicio 1
def listaPares(num1, num2):
    for n in range(1, 21):
        if n % 2 == 0:
            print(n, end=' ')


# In[7]:


listaPares(1, 21)


# In[34]:


#Exercício 2
nome = 'joas'
def maiusculo(nome):
    print(nome.upper())


# In[35]:


maiusculo(nome)


# In[50]:


#Exercicio 3
n = [1, 2, 3, 4]
def listaElementos(n):
    n.append('Joás')
    n.append('Feitosa')
    print(n)


# In[51]:


listaElementos(n)


# In[52]:


#Exercicio 4
s = 'sua lista é: '
lis = [1, 2, 3, 4]
def listaElementos2(s, lis):
    print(lis[0])
    print(lis)


# In[53]:


listaElementos2(s,lis)


# In[55]:


#Exercicio 5
s = 'soma'
def anonima(s):
    s = 2+4
    print(s)


# In[70]:


anonima(s)


# In[57]:


#Exercicio 6
total = 0
def soma( arg1, arg2):
    total = arg1 + arg2;
    print("Dentro da função o total é", total)
    return total


# In[58]:


soma(1,3)


# 

# In[61]:


#Exercicio 7
Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = map(lambda x: ((x * 9/5) + 32), Celsius)
print (list(Fahrenheit))


# In[62]:


#Exercicio 8
def dicionario(d):
    print(dir(d))


# In[63]:


d = {'nome':"Joas"}


# In[74]:


print(d)


# In[65]:


#Exercicio 9
import pandas as pd
dir(pd)


# In[79]:


#Exercicio 10 - Desafio
import pandas as pd
file_name = 'C:\\Users\\Aluno\\Documents\\binary.csv'


# In[81]:


pip install pandas


# In[ ]:




