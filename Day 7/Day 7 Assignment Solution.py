# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 23:53:56 2020

@author: ritesh
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataSet = pd.read_csv('general_data.csv')

print(dataSet.head())
dataSet.head()
dataSet.columns
dataSet.isnull()
dataSet.duplicated()
dataSet
dataSet.info()
dataSet.drop_duplicates()
dataSet2 = dataSet.describe()
dataSet2
dataSet2.mode()
dataSet2['Age'].mode()
dataSet['Age'].mode()
dataSet.mode()
dataSet['Age'].mode()
dataSet[['Age','DistanceFromHome','Education','MonthlyIncome',
'NumCompaniesWorked', 'PercentSalaryHike','TotalWorkingYears', 'TrainingTimesLastYear',
'YearsAtCompany','YearsSinceLastPromotion', 'YearsWithCurrManager']].mode()
dataSet3 = dataSet[['Age','DistanceFromHome','Education','MonthlyIncome',
'NumCompaniesWorked', 'PercentSalaryHike','TotalWorkingYears', 'TrainingTimesLastYear',
'YearsAtCompany','YearsSinceLastPromotion', 'YearsWithCurrManager']].mode()
plt.boxplot(dataSet.Age)
plt.boxplot(dataSet.MonthlyIncome)