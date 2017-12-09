import os.path
import os, FileSystemMonitorDeamon
import time

def encryptFile(filename, emailID):
	#get public key for the user
	encryptDate(filename, emailID)
	



def main():
	emailID1 = "sfad@fg.com"
	emailID2 = "vgop@fg.com"
	filename = FileSystemMonitor.getFileName()
	timeBefore = time.now()
	encryptFile()	
	timeAfter = time.now()
	deltaEncryption = timeAFter - timeBefore 

if __name__ == "__main__":
	main()
