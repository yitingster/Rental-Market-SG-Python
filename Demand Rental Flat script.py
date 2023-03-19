#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
import matplotlib.pyplot as plt

print("*** Demand for Rental and Sold Flats ***")
print()

### Importing Demand for Rental Flat ###
demand_path = "C:/Users/Yi Ting/Desktop/CA1/raw data/demand-for-rental-and-sold-flats.csv"
demand = np.genfromtxt(demand_path, delimiter=',', skip_header=True,
                  dtype=[('start_year', 'i4'),('end_year', 'i4'),('type','U20'),('demand','i8')])


### Overview of Data ###
print("*Overview of data")
print()
print("There are {} rows in this dataset".format(len(demand)))

start_yr = set(demand['start_year'])
end_yr = set(demand['end_year'])
flat_type = set(demand['type'])
d = set(demand['demand'])

### Unique values ###
print()
print("There are {} unique values in start_year column.".format(str(len(start_yr))))
print("There are {} unique values in end_year column.".format(str(len(end_yr))))
print("There are {} unique values in type column.".format(str(len(flat_type))))
print("There are {} unique values in demand column.".format(str(len(d))))

print()


### Check for missing value ###

def missing(data, column):  
    for num in data[column]:
        if num == -1: 
            return print("There are missing values in {} column.".format(column))
        else: 
            return print("There are no missing values in {} column.".format(column))
        
missing(demand, 'demand') #output: There are no missing values


### Check for data consistency ###

#Extract demand for rental flats
demand_rental = demand[demand['type'] == 'rental_flats' ]

#Extract data from 2006 onwards, the year range of interest
demand_rental = demand_rental[demand_rental['start_year'] >= 2006]

#Year range
interval = (demand_rental['end_year'][0] - demand_rental['start_year'][0])+1

#Check if interval is consistent
print()
print('Check if data is consistent in each row:')
for num in range(len(demand_rental)):
    if demand_rental['end_year'][num] - demand_rental['start_year'][num] + 1 == interval:
        print('Data is consistent')
    else:
        print('Data is inconsistent')


### Statistic Overview of Data ###
print()
print("*Statistic overview of data")
print()
print("The data are from the year of {} to {}.".format(min(start_yr), max(end_yr)))


print("The demand from each row is the sum of {} years of data but it is inconsistent.".format(interval))
print("Mean demand from the year of 2006 to {}: {:.0f}".format(demand_rental['end_year'].max(), demand_rental['demand'].mean()))

median = np.median(demand_rental['demand'])
print("Median demand from the year of 2006 to {}: {:.0f}".format(demand_rental['end_year'].max(), median))

std_dv = np.std(demand_rental['demand'])
print("Standard Deviation: {:.0f}".format(std_dv))


### Graph plotting ###
print()
print('*Graph')
print()

#Bar Chart 1

#Create year range label
yr_label = np.array(['2006 - 2010', '2011-2015', '2016-2017', '2018-2019'])

#Demand 
dd = demand_rental['demand']

#Graph plot
plt.figure(figsize = (12,8))
bar = plt.bar(yr_label,dd, width = 0.45)   
plt.ylabel('Demand', fontsize = 12)
plt.title('Demand for rental flat from year 2006 - 2019', fontsize = 14, fontweight = 'bold')

#Total demand text label
x = 0
for y in dd:
    plt.text(x-0.08, y, str(y), fontsize = 11)
    x = x + 1

#Change colour
colors = ["red", "green", "blue", "purple"]

for i in range(len(yr_label)):   
    bar[i].set_facecolor(colors[i])
    
plt.show()


#Bar Chart 2

#Create year range label
yr_label = np.array(['2006 - 2010', '2011-2015', '2016-2019'])

#Demand, combining 2016-2019 to make data more consistent
dd2 = np.array([dd[0], dd[1], dd[2] + dd[3]])

#Graph plot
plt.figure(figsize = (12,8))
bar = plt.bar(yr_label,dd2, width = 0.45, color = '#ff69b4')   
plt.ylabel('Demand', fontsize = 11)
plt.title('Demand for rental flat from year 2006 - 2019', fontsize = 14, fontweight = 'bold')

#Total demand text label
x = 0
for y in dd2:
    plt.text(x-0.08, y, str(y), fontsize = 11)
    x = x + 1

    
#Change colour
colors = ["red", "green", "blue"]

for i in range(len(yr_label)):   
    bar[i].set_facecolor(colors[i])    
    
plt.show()

