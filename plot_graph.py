import matplotlib.pyplot as plt
import numpy as np

numFiles = [1, 10, 100, 500, 1000, 2000, 4000]
avgTime = [0.002681016922, 0.00439212322235, 0.00621670007706, 0.00709121370316, 0.00695849990845, 0.00781035757065, 0.00731262212992]

y_pos = range(len(numFiles))
bar_width = 0.5
#plt.plot(numFiles, avgTime)
plt.bar(numFiles, avgTime, width=200, align='center', alpha=0.3)
#plt.xticks(y_pos, numFiles)
plt.xlabel('Number of Files encrypted')
plt.ylabel('Average Time')
plt.title('Encryption time plot')
plt.axis([0, max(numFiles), 0, max(avgTime)])

plt.show()
