import math
import numpy as np
import statistics as stat

files = ["../2018-1-25-15.14_data_Ne.dat",
        "../2018-1-25-15.9_data_Ne.dat",
        "../2018-1-25-15.18_data_Ne.dat",
        "../2018-1-25-15.27_data_Ne.dat",
        "../2018-1-25-15.4_data_Ne.dat",
        "../2018-1-25-15.23_data_Ne.dat",
        "../2018-1-25-16.0_data_Hg%0D%0A.dat",
        "../2018-1-25-16.4_data_Hg%0D%0A.dat",
        "../2018-1-25-17.55_data_Hg%0D%0A.dat",
        "../2018-1-25-18.2_data_Hg%0D%0A.dat",
        "../2018-1-25-15.52_data_Hg%0D%0A.dat",
        "../2018-1-25-15.57_data_Hg%0D%0A.dat"]

fout = open("3feladat.txt",'w')

width = 3 # in this range left and right will the script compare numbers
maxes = []
allDistances = []
for f in range(6, len(files)): # in all files
    data = np.loadtxt(files[f], skiprows=8)
    localMaxPlaces = [] # the x value at the max
    localMaxValues = [] # the f(x) value at the max

    for i in range(width, len(data)-width): # looks at every value
        isMax = True                        # by default it is a local max
        for j in range(-width, width):      # compares it to neighbours left and right within 'width'
            # to find plateaus use > here 
            if j != 0 and data[i+j][1] >= data[i][1]:
                isMax = False               # if any neighbour is bigger, it is no more a local max
        if isMax:
          localMaxPlaces.append(data[i][0]) # collecting local maxes in a list
          localMaxValues.append(data[i][1])
        
    distanceOfMaxes = []
    for i in range(1, len(localMaxPlaces)):
        distanceOfMaxes.append(localMaxPlaces[i] - localMaxPlaces[i-1])
        allDistances.append(localMaxPlaces[i] - localMaxPlaces[i-1])

    maxes.append(localMaxValues)

    print(files[f], " : ")
    for d in distanceOfMaxes:
        print(d)
    print(" ")

print("Distances:")
for d in range(len(allDistances)):
    try:
        if allDistances[d] < 10: allDistances.pop(d)
    except:
        pass

for d in allDistances:
    print(d)

print("Mean: {}; Standard deviation: {}".format(stat.mean(allDistances), stat.pstdev(allDistances)))

#fout.write("{} {} {}\n".format(temps[f], peak, 1/peak))
#print("Peak of the '{}':\t {}, {}, {}".format(files[f], listOfDatas[pI1][0], listOfDatas[pI2][0], listOfDatas[pI3][0]))
#print("LM of '{}': {}".format(files[f], locmaxes))
    