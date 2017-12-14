import matplotlib.pyplot as plt
import numpy as np
import os, sys

numFiles = [1, 10, 100, 500, 1000, 2000, 4000]
numFilesbar2 = map(lambda x:x+200, numFiles)
avgTime = [0.002681016922, 0.00439212322235, 0.00621670007706, 0.00709121370316, 0.00695849990845, 0.00781035757065, 0.00731262212992]
avgTime2 = [0.0119068622589, 0.0129016876221, 0.0124660086632, 0.0124842896461,  0.0136637945175,  0.0123260861635, 0.0123281091452]
stdDevEnc = [0.00018388492719341947, 0.00025376571368744078, 0.00011331372220662978, 3.9082478279393022e-05, 0.00039358891772538332, 0.00028649386533868956, 5.224722831151822e-05]
stdDevDec = [0, 0.00139621787504, 0.000660481959529, 0.000814150598532, 0.00655269418534, 0.00208470978633, 0.00202869676072]


def graphPlot(typeGraph):

	if typeGraph == "line":
		plt.plot(numFiles, avgTime, 'b', label='Encryption')
		plt.plot(numFiles, avgTime2, 'r', label='Decryption')
		plt.plot(numFiles, stdDevEnc, 'g', label='Std. Dev. Encryption')
		plt.plot(numFiles, stdDevDec, 'm', label='Std. Dev. Decryption')
		plt.legend(loc='upper right', shadow=True)
	elif typeGraph == "bar":
		plt.bar(numFiles, avgTime, width=200, color='b', align='center', alpha=0.3)
		plt.bar(numFilesbar2, avgTime2, width=200, color='r', align='center', alpha=0.3)
	plt.xticks(np.arange(min(numFiles), max(numFiles)+200, 500.0))
	plt.xlabel('Number of Files encrypted')
	plt.ylabel('Average Time')
	plt.title('Encryption-Decryption-StdDev time plot')
	plt.axis([0, max(numFiles)+500, 0, max(avgTime)+0.01])
	plt.show()

def main():
		
	graphPlot(sys.argv[1])

if __name__ == "__main__":
	main()
