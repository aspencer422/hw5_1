#-------------------------------------------------------------------------
# AUTHOR: Anthony Spencer
# FILENAME: clustering.py
# SPECIFICATION: run k means on test data
# FOR: CS 4210- Assignment #5
# TIME SPENT: 1hour
#-----------------------------------------------------------*/

#importing some Python libraries
from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score
from sklearn import metrics


df = pd.read_csv('training_data.csv', sep=',', header=None) #reading the data by using Pandas library

#assign your training data to X_training feature matrix
X_training=df
#run kmeans testing different k values from 2 until 20 clusters
ks=[]
s_coef=[]
for i in range(11):
     if i > 0:
          k = 2*i
     #Use:  
          kmeans = KMeans(n_clusters=k, random_state=0)
     #      
     # 
          kmeans.fit(X_training)
     #--> add your Python code


     #for each k, calculate the silhouette_coefficient by using: silhouette_score(X_training, kmeans.labels_)
     #find which k maximizes the silhouette_coefficient
     #--> add your Python code here
          temp = silhouette_score(X_training, kmeans.labels_)
          s_coef.append(temp)
          ks.append(str(k))

#plot the value of the silhouette_coefficient for each k value of kmeans so that we can see the best k
#--> add your Python code here=
plt.plot(ks,s_coef, color='blue', marker='o', linestyle='solid')
plt.show()
#reading the validation data (clusters) by using Pandas library
#--> add your Python code here

#assign your data labels to vector labels (you might need to reshape the row vector to a column vector)
# do this: np.array(df.values).reshape(1,<number of samples>)[0]
#--> add your Python code here
df2 = pd.read_csv('testing_data.csv', sep=',', header=None)
labels=[]
for i in range(len(df2)):
     labels.append(df2[0][i])
#Calculate and print the Homogeneity of this kmeans clustering
print("K-Means Homogeneity Score = " + metrics.homogeneity_score(labels, kmeans.labels_).__str__())
#--> add your Python code here

#rung agglomerative clustering now by using the best value o k calculated before by kmeans
#Do it:
agg = AgglomerativeClustering(n_clusters=10, linkage='ward')
agg.fit(X_training)

#Calculate and print the Homogeneity of this agglomerative clustering
print("Agglomerative Clustering Homogeneity Score = " + metrics.homogeneity_score(labels, agg.labels_).__str__())
