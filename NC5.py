import numpy as np
data = np.genfromtxt('emails.csv', delimiter=',', encoding = None, dtype='unicode')
X = data
# Sort X into array that have maximum texting
t = X.astype(float) #Turn data to float
h = t.astype(int)   #turn data to integer
sort = np.argsort(-h, axis = 1) #Sort data with Descending order
print('Note that python index is starting with 0, so to find group for id number in csv file, you must -1 it in python')
print('For example: Number 9 in csv file is corresponding to 8 in python')
id = int(input('Find crewmate Number in python: '))
#Choose some first possible group by id, and number of people has most frequent mailing
#number of people should be around 8 to 12, to get more accuracy. More of it will increase the execution time
def find_best_crewmate(id, num_member):
  a = sort[id, :19]
  member = np.array([id])
  b = np.array([a[0]])
  t=0
  while np.size(member,0) < num_member:
    if np.any(member == b[t]):
      t += 1
    else:
      t = 0
    member = np.append(member, b[t])
    b = sort[a[t], :19]
    a = b
  return member

#Printing a group from a specific member, and their most frequent mailing
def find_group(x, u):
  group = np.array([])
  mean = u
  num = np.size(x, 0)
  i = 0 #intial counter
  stop = 0 #stop the while loop
  #Find the number of member in that group
  while True:
    if mean == np.size(sort,0):
      print("You get something wrong, please debug it")
      #This appears when the code is error
      break
    if i == num:
      mean -=1
      stop = 1
      i =0
    arr = np.in1d(sort[x, :mean], sort[x[i],(mean -1)])
    count = np.count_nonzero(arr)
    if count >= num-2:
      if stop ==1:
        break
      else:
        mean+=1
        i= 0
    else:
      i+= 1
#Add member in the same group, by choosing the frequency they appear
  for i in range(num):
    if np.size(group,0) < mean +1:
      for k in range(mean):
        arr = np.in1d(sort[x, :mean], sort[x[i],k])
        count = np.count_nonzero(arr)
        if count >= (num-2):
          if np.any(group == sort[x[i],k]):
            continue
          else:
            group = np.append(group, sort[x[i],k])
        else:
          continue
    else:
      break
  group = group.astype(int) #return in integer mode for easy look
  return group, mean

member = find_best_crewmate(id, 10)
# print(member)
group, mean = find_group(member, 25)

print('Crewmate id ' + str(id) +' in python is in group with: ')
print(group)
print('Total number of people in this group: ', np.size(group, 0))

