# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 20:21:38 2019

@author: Aluno
"""

from sklearn.model_selection import train_test_split

#seleção de variáveis preditoras (Future Selection)
atributos = ['num_preg', 'glucose_conc', 'diastolic_bp', 'thickness', 'insulin', 'bmi', 'diab_pred', 'age']

#Variável a ser prevista
atrib_prev = ['diabetes']

#Criando objetos
x = df[atributos].values
y = df[atrib_prev].values