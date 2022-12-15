  #*********************************************************************
#Comsc230 final data set analysis
#Zayvier Hartman, Liam Reynolds
#Dr. Omar Rivera Morales
#This program takes information from our data set and analyzes the information
# utilizing the functions given by the pandas library in python
#
##
#PANDAS DID NOT WORK FOR US, ALL CODE WAS DONE IN JUPYTER NOTEBOOK,
#WE INTERCHANGED THE VARIABLES IN THE SCATTER PLOT FUNCTION TO GET ALL OF OUR GRAPHS
#THESE VALUES WILL BE COMMENTED NEXT TO LINES ACCORDINGLY
#**********************************************************************

import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

data = pd.read_csv('cleveland.csv')#Read CSV file from folder

data.sort_values(by='Cholesterol',axis=0,ascending=True) #Sorts Data table by Cholesterol smallest to highest

#get scatter graph for Cholesterol to Diagnosis
number = data.select_dtypes(include ='number')

number.iloc[4,11] #index values 2-Pain Type, 3-Resting Blood Pressure, 4- Cholesterol, 7-Max HR, 11- Diagnosis

selections =['Cholesterol','Diagnosis']# changed strings to match indexed columns from previous line
df = data[selections]

g = sb.PairGrid(df)# call seaborn to combine columns data
g.map(plt.scatter); #Create Scatter Plots

data['Diagnosis'].value_counts()
data['PainType'].value_counts()
