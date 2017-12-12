import matplotlib.pyplot as plt
import numpy as np
import os, sys

numFiles = [1, 500, 1000, 2000, 4000]
numFilesbar2 = map(lambda x:x+200, numFiles)
avgTime = [0.002681016922, 0.00709121370316, 0.00695849990845, 0.00781035757065, 0.00731262212992]
avgTime2 = [0.0134689807892, 0.0123686718941, 0.0125782625675,  0.0122886763811, 0.0136354961991]

def graphPlot(typeGraph):

	if typeGraph == "line":
		plt.plot(numFiles, avgTime)
		#plt.plot(numFiles, avgTime2)
	elif typeGraph == "bar":
		plt.bar(numFiles, avgTime, width=200, color='b', align='center', alpha=0.3)
		plt.bar(numFilesbar2, avgTime2, width=200, color='r', align='center', alpha=0.3)
	plt.xticks(np.arange(min(numFiles), max(numFiles)+200, 500.0))
	plt.xlabel('Number of Files encrypted')
	plt.ylabel('Average Time')
	plt.title('Encryption time plot')
	plt.axis([0, max(numFiles)+500, 0, max(avgTime)+0.01])
	plt.show()

def main():
		
	graphPlot(sys.argv[1])

if __name__ == "__main__":
	main()
