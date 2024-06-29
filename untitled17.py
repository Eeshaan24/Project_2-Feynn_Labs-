# -*- coding: utf-8 -*-
"""Untitled17.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Nv6jZ-fpalasIw0rgdpUAL66WILiewtR
"""

import numpy as np
import pandas as pd
import seaborn as sns

data = pd.read_csv('/content/indian-auto-mpg.csv')

data.head()

data.info()

data.isnull().sum()









data.replace({"Location":{'Ahmedabad':1, 'Bangalore':2, 'Chennai':3, 'Coimbatore':4, 'Delhi':5, 'Hyderabad':6, 'Jaipur':7, 'Kochi':8, 'Kolkata':9, 'Mumbai':10, 'Pune':11}}, inplace = True)

data.head()

data.groupby('Manufacturer').count()

x = data.iloc[:,[3,13]].values

from sklearn.cluster import KMeans
wcss = []

for i in range(1,11):
  kmeans = KMeans(n_clusters=i, init = 'k-means++', random_state=0)
  kmeans.fit(x)
  wcss.append(kmeans.inertia_)

import matplotlib.pyplot as plt

plt.plot(range(1,11), wcss)
plt.title('The Elbow Method')
plt.xlabel('No. of clusters')
plt.ylabel('WCSS')
plt.show()

kmeansmodel = KMeans(n_clusters=3, init = 'k-means++', random_state=0)

y_kmeans = kmeansmodel.fit_predict(x)



plt.scatter(x[y_kmeans==0,0], x[y_kmeans == 0,1], s=80, c='red', label = 'Customer_Cluster 1')
plt.scatter(x[y_kmeans==1,0], x[y_kmeans == 1,1], s=80, c='blue', label = 'Customer_Cluster 2')
plt.scatter(x[y_kmeans==2,0], x[y_kmeans == 2,1], s=80, c='yellow', label = 'Customer_Cluster 3')
#plt.scatter(x[y_kmeans==3,0], x[y_kmeans == 3,1], s=80, c='black', label = 'Price 4')

#plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], s=100, c='magenta', label = 'Centroids')

plt.title("Cluster of price")
plt.xlabel('Location')
plt.ylabel('Price')
plt.xlim(0,12)
plt.ylim(0,200)
plt.legend()
plt.show()

data.replace({'Transmission':{1:'Manual' , 2:'Automatic'}}, inplace=True)

data.head()

k = data.iloc[:,[3,7]].values
k

wcss2 = []

for i in range(1,11):
  kmeans2 = KMeans(n_clusters=i, init = 'k-means++', random_state=0)
  kmeans2.fit(k)
  wcss2.append(kmeans2.inertia_)

plt.plot(range(1,11), wcss2)
plt.title('The Elbow Method')
plt.xlabel('No. of clusters')
plt.ylabel('WCSS2')
plt.show()

kmeansmodel2 = KMeans(n_clusters=3, init = 'k-means++', random_state=0)

y_kmeans2 = kmeansmodel2.fit_predict(k)

ax = sns.countplot(x='Transmission', data=data)

for bars in ax.containers:
  ax.bar_label(bars)

ax = sns.countplot(data = data, x = 'Location', hue = 'Transmission')

for bars in ax.containers:
    ax.bar_label(bars)

sales_state = data.groupby(['Location'], as_index=False)['Price'].sum().sort_values(by='Price', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = sales_state, x = 'Location',y= 'Price')

data.replace({'Owner_Type':{'First':1 , 'Second':2, 'Third':3, 'Fourth':4}}, inplace=True)
data.head()

x2 = data.iloc[:,[8,13]].values
x2

kmeansmodel3 = KMeans(n_clusters=3, init = 'k-means++', random_state=0)

y_kmeans3 = kmeansmodel3.fit_predict(x2)

plt.scatter(x2[y_kmeans3==0,0], x2[y_kmeans3 == 0,1], s=80, c='red', label = 'Customer_Cluster 1')
plt.scatter(x2[y_kmeans3==1,0], x2[y_kmeans3 == 1,1], s=80, c='blue', label = 'Customer_Cluster 2')
plt.scatter(x2[y_kmeans3==2,0], x2[y_kmeans3 == 2,1], s=80, c='yellow', label = 'Customer_Cluster 3')
#plt.scatter(x[y_kmeans==3,0], x[y_kmeans == 3,1], s=80, c='black', label = 'Price 4')

#plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], s=100, c='magenta', label = 'Centroids')

plt.title("Clustering")
plt.xlabel('Owner')
plt.ylabel('Price')
#plt.ylim(0,25)
plt.legend()
plt.show()

ax = sns.countplot(data = data, x = 'Location', hue = 'Owner_Type')

for bars in ax.containers:
    ax.bar_label(bars)

ax = sns.countplot(data = data, x = 'Location', hue = 'Seats')

for bars in ax.containers:
    ax.bar_label(bars)

sns.heatmap(data.corr(), annot=True)

sns.pairplot(data)

