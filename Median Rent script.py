#!/usr/bin/env python
# coding: utf-8

# In[89]:


import numpy as np
import matplotlib.pyplot as plt

print("*** Median rent by town and flat type ***")
print()

### Importing Median rent by town and flat type ###
median_path = "C:/Users/Yi Ting/Desktop/CA1/raw data/median-rent-by-town-and-flat-type.csv"
median = np.genfromtxt(median_path, delimiter=',', skip_header=True,
                  dtype=[('qtr', 'U7'),('town', 'U30'),('type','U20'),('price','i4')])


### Overview of Data ###

print("*Overview of data")
print()
print("There are {} rows in this dataset".format(len(median)))

qtr = set(median['qtr'])
town = set(median['town'])
room_type = set(median['type'])
price = set(median['price'])

# Unique Values
print()
print("There are {} unique values in qtr column.".format(str(len(qtr))))
print("There are {} unique values in town column.".format(str(len(town))))
print("There are {} unique values in type column.".format(str(len(room_type))))
print("There are {} unique values in price column.".format(str(len(price))))

print()

### Check for missing value ###

def missing(data, column):  
    for num in data[column]:
        if num == -1: 
            return print("There are missing values in {} column.".format(column))
        else: 
            return print("There are no missing values in {} column.".format(column))
    
missing(median, 'price') #output: There are missing value

#remove missing values
median2 = median[median['price'] != -1]



### Statistic Overview of Data ###
print()
print("*Statistic overview of data")

#Extracting year from qtr columns
year = []
for i in qtr:
    year.append(i[:4])
    
#Statistic overview
print()
print("The data are from the year of {} to {}.".format(min(year), max(year)))
print("The rental price range from ${:.2f} to ${:.2f}.".format(median2['price'].min(),median2['price'].max()))
print("The mean rental price is ${:.2f}.".format(median2['price'].mean()))

median = np.median(median2['price'])
print("The median rental price is ${:.2f}.".format(median))

std_dv = np.std(median2['price'])
print("The standard deviation {:.2f}.".format(std_dv))


### Graph plotting ###
print()
print('*Graph')
print()

#Box and Whisker Chart
print('Box and Whisker chart: Price of Room Type.')

# Price of different room type
print()
print("There are only 5 room types after removing the missing values, 1-Room type is removed.")
print("The 5 room types are: {}.".format(set(median2['type'])))


#Spliting room type 
median2 = median2[4271:]
r2 = median2[median2['type'] == '2-RM']
r3 = median2[median2['type'] == '3-RM']
r4 = median2[median2['type'] == '4-RM']
r5 = median2[median2['type'] == '5-RM']
exe = median2[median2['type'] == 'EXEC']

#Extracting room price by type and labels for plot
room_price = np.array([r2['price'], r3['price'], r4['price'], r5['price'], exe['price']])
labels = np.array(['2-Room', '3-Room', '4-Room','5-Room','Exec'])

#Graph ploting 
box_plot = plt.boxplot(room_price, labels = labels, patch_artist = True)

#change colour
colours = ['pink', 'lightblue','lightgreen', 'lightsalmon', 'plum']
patchcolor = list(zip(box_plot['boxes'], colours))
for patch, color in patchcolor:
    patch.set_facecolor(color)

#Label Median
for line in box_plot['medians']:
    x, y = line.get_xydata()[1] 
    plt.text(x, y, 'Median:{:.0f}'.format(y),
         horizontalalignment='center',fontsize=8)

#Labelling box plot    
plt.title('Price of Room Type')
plt.ylabel('Price ($)')

plt.show()

#Line Chart
print()
print('Line chart of Median price from 2005 to 2020.')

#Change quarter column into year
year = []
median3 = median2.copy()
for i in median2['qtr']:
    year.append(int(i[:4]))

median3['qtr'] = year
year_unique = sorted(list(set(year)))

#Line plot

yearly_price = np.bincount(np.searchsorted(year_unique,median3['qtr']), median3['price'])
yearly_label = np.array(year_unique)

plt.ylabel('Median Price')
plt.title("Median price of room flat from year 2005 to 2020")

plt.plot(yearly_label,yearly_price)
plt.show()


# In[ ]:




