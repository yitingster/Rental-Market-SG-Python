#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
import matplotlib.pyplot as plt

### Importing Median rent by town and flat type ###
print("*** Renting out of flat approvals by flat type quarterly***")
approval_path = "C:/Users/Yi Ting/Desktop/CA1/raw data/renting-out-of-flat-approvals-by-flat-type-quarterly.csv"
approval = np.genfromtxt(approval_path, delimiter=',', skip_header=True,
                  dtype=[('quarter', 'U7'),('type','U20'),('approval','i8')])


### Overview of Data ###
print()
print("*Overview of data")
print()
print("There are {} rows in this dataset".format(len(approval)))

qtr = set(approval['quarter'])
flat_type = set(approval['type'])
a = set(approval['approval'])

#Unique Values
print()
print("There are {} unique values in quarter column.".format(str(len(qtr))))
print("There are {} unique values in type column.".format(str(len(flat_type))))
print("There are {} unique values in approval column.".format(str(len(a))))


### Check for missing value ###

def missing(data, column):  
    for num in data[column]:
        if num == -1: 
            return print("There are missing values in {} column.".format(column))
        else: 
            return print("There are no missing values in {} column.".format(column))

print()        
missing(approval, 'approval') #output: There are no missing values


### Statistic Overview of Data ###
print()
print("*Statistic overview of data")
print()

#Extracting year from qtr columns
year = []
for i in qtr:
    year.append(i[:4])

#Statistic Overview
print("The data are from the year of {} to {}.".format(min(year), max(year)))
print("Mean approval: {:.0f}".format(approval['approval'].mean()))

for i in flat_type:
    print("Mean approval of {}: {:.0f}".format(i, approval[approval['type'] == i]['approval'].mean()))

median = np.median(approval['approval'])
print("Median approval: {:.0f}".format(median))

std_dv = np.std(approval['approval'])
print("Standard Deviation: {:.0f}".format(std_dv))


### Graph plotting ###
print()
print('*Graph')
print()
#Line plot 
print('Line chart of yearly rental flat approval.')
#get yearly data
approval_yr = []
start = 0
end = 23
for num in range((2020-2007)+1):
    approval_yr.append(approval['approval'][start:end+1].sum())
    start += 24
    end += 24
    
#remove last year incomplete data
approval_yr = np.array(approval_yr[:-1])

#create year label
year_label = np.array(list(range(2007,2020)))

#plot 
fig = plt.figure(figsize = (12,8))
fig.suptitle('Yearly Rental Flat Approval', fontsize=14, fontweight='bold')

ax = fig.add_subplot(111)
fig.subplots_adjust(top=0.95)

ax.set_xlabel('Year', fontsize = 14)
ax.set_ylabel('Rental Approval', fontsize = 14)

plt.axis([2008, 2020, 10000, 50000])

plt.plot(year_label, approval_yr,'g', linewidth = 3)
plt.show()


#Pie Chart
print()
print('Pie chart of 2020 flat type')

#Get sum of approval for each room type
y_2020 = approval[-12:]
room1 = y_2020[y_2020['type']== '1-room']['approval'].sum()
room2 = y_2020[y_2020['type']== '2-room']['approval'].sum()
room3 = y_2020[y_2020['type']== '3-room']['approval'].sum()
room4 = y_2020[y_2020['type']== '4-room']['approval'].sum()
room5 = y_2020[y_2020['type']== '5-room']['approval'].sum()
exe = y_2020[y_2020['type']== 'Executive']['approval'].sum()

#combining data
flats = np.array([room1,room2,room3,room4,room5,exe])
flats_label = np.array(['1-room', '2-room','3-room', '4-room', '5-room','Executive'])

#plot
fig1, ax1 = plt.subplots()
ax1.pie(flats, labels= flats_label, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')
fig1.suptitle('2020 Approval by Room Type', fontsize=12, fontweight='bold')
fig1.subplots_adjust(top=0.85)
plt.show()



# In[ ]:




