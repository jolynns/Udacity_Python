# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

Petals = [15, 16, 17,
          16, 21, 22,
          15, 16, 15,
          17, 16, 22,
          14, 13, 14,
          14, 15, 15,
          14, 15, 16,
          10, 19, 15,
          15, 22, 24,
          25, 15, 16]

print(Petals)


# get the number of variables
PetalsLen = len(Petals)

# Find the most frequent variable
from collections import Counter

cnt = Counter(Petals)
MostComm = (cnt.most_common(1))
PetalsCnt = [x[0] for x in MostComm]
print ("The most common petal count is: " + str(PetalsCnt[0]))

# Find the frequentcy of flowers with 15 petals

PetalsFreq = [x[1] for x in MostComm]
print ("The frequency of flowers with 15 petals is: " + str(PetalsFreq[0]))

# Find the proportion of flowers with 15 petals

PetalProp = float(PetalsFreq[0])/PetalsLen
print ("The proportion of flowers with 15 petals is: " + str(PetalProp))

# Find the percentage of flowers with 15 petals

PetalPerc = PetalProp * 100
print ("The percent of flowers with 15 petals is: " + str(PetalPerc) + "%")

# Create a historgram
import matplotlib.pyplot as plt

# with a bin size of 2
plt.hist(Petals, bins=(int(PetalsLen)/2))
plt.show()

# with a bin size of 5
plt.hist(Petals, bins=(int(PetalsLen)/5))
plt.show()





