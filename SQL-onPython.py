##################################################################
# Author: Andrew Leon                                            # 
# Date 10/20/22                                                  #
# Purpose: to establish a connection to an SQL database and      #
# perform SQL queries within a python program                    #
##################################################################
# py -m venv venv to create a new virtual environment
# pip install openpyxl
# 
# required modules
# please install anaconda in order to install Pandas: https://www.anaconda.com/
# please install Pandas by using Anaconda cmd Prompt: conda install pandas
from csv import excel
import pandas as pd
excel_file = 'HD2020.xlsx'

df = pd.read_excel(excel_file)
print(df.head(10)) # prints first 10 items from data set
print('--------------------------------------',
'\n', 'All columns in data set')
print(df.info())

#df.loc[df['STABBR'] == 'NC'].sum()