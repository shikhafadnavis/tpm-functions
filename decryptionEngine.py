import tpm_script as tpmFunctions
import os, sys, time
import glob

#################################
# Holding Global variable here
emailID1 = "sfad@fg.com"
emailID2 = "vgop@fg.com"
rootDirectory = "/home/sfubuntu1422/mfsdummy"
space = " "
#TODO Encrypted private key file name
filename_keyblob = " "

def _getCurrentTime():
	return time.now()

def main():
	
	privateKey = tpmFunction.decryptPrivateKeyUsingTPM(filename_keyblob)
	os.chdir("/home/sfubuntu/tpm-functions/")
	for file in glob.glob("*.txt.gpg"):
		timeBefore = _getCurrentTime()
		# TODO Change decryptData functions in tpm_script and remove raw_input
		tpmFunctions.decryptData(file,privateKey)
		timeAfter = _getCurrentTime()
		deltaDecryption = timeAfter - timeBefore
		print "Operation took %s seconds" % deltaDecryption
		
	
if __name__=="__main__":
        main()


