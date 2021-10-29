from sklearn.cluster import KMeans
import numpy as np
data = np.genfromtxt('senate.csv', delimiter=',',encoding = None, dtype='unicode')
X = data[1:,3:]
# Choosing number of cluster, size = 2 to cluster two groups.
# size = 3 to cluster three groups, and find the remaining small group
print('This program help to cluster voting group')
print('Press 2 to cluster two groups')
print('Press 3 to cluster two groups and the small remaining group')
size = int(input('Insert number of clusting group: '))
kmeans = KMeans(n_clusters=size, random_state=0).fit(X)
#print the label for each data
label = kmeans.labels_
#print the expected label result
a = data[1:,1]
# The number of correct output
t= 0
# The number of false output
f = 0
# Suspicious array
sus = []
if size == 2:
# when size = 2. label = 0 means that this data is in R group,
# while label = 1 means that this data is in D group
  for i in range (a.size):
    if a[i] == 'R' and label[i] == 0:
      t = t + 1
    elif a[i] == 'D' and label[i] == 1:
      t = t + 1
    else:
      f = f+ 1
      sus.append(i) #Collect suspicious object
if size == 3:
# when size = 3. label = 1 means that this data is in R group
# while label = 0 means that it is in D group
# and label = 2 means that it is in the remaining small group
  for i in range (a.size):
    if a[i] == 'R' and label[i] == 1:
      t = t + 1
    elif a[i] == 'D' and label[i] == 0:
      t = t + 1
    else:
      f = f+ 1
      sus.append(i) #Collect suspicious object

print('Number of correct output is: ',t)
if size == 2:
  print('Number of incorrect output is: ',f)
  print('The incorrect index outputs are: ')
  print(sus)
if size ==3:
  print('Number of remaining group is: ', f)
  print('The remaining group index outputs are: ')
  print(sus)
print('Note that the index output in python must plus (+) 2 to get the actual result (with file csv)')
print('For example: 42 in python is corresponding to line 44 in csv file')