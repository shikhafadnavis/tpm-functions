import os, time
import gnupg, sys
from pprint import pprint
import glob, numpy

######################

# Globally held data 
# These can be overwritten by the API
FILENAME = "mykey.asc"
DEBUG = True
# TODO - Change the monitoring directory name
master_list = []
# MODE = 1 for encryption and 2 for decryption
ROOT_MODE = 1
MODE = 1
ROOT_DIRECTORY_V = "./"

# Global GPG Initialization

if os.path.exists("/home/testgpguser/gpghome"):
	os.system("rm -r /home/testgpguser/gpghome")

gpg = gnupg.GPG(gnupghome="/home/testgpguser/gpghome")

# User space routines
def createKey():
        
	input_data = gpg.gen_key_input(key_type = "RSA", key_length = 2048, name_email = 'venky@fg.com', passphrase = 'venky')

        return gpg.gen_key(input_data)
        

def exportKey(key,fileName):
	ascii_armored_public_keys = gpg.export_keys(str(key))
        ascii_armored_private_keys = gpg.export_keys(str(key), True)

        with open(fileName, 'w') as f:
                f.write(ascii_armored_public_keys)
                f.write(ascii_armored_private_keys)


def importKeysIntoGPG(fileName, flag):

        key_data = open(fileName).read()
        import_result = gpg.import_keys(key_data)
	
	if flag:
	        pprint(import_result.results)

def listAvailableKeys():

        public_keys = gpg.list_keys()
        private_keys = gpg.list_keys(True)

        print "Public keys: "
        pprint(public_keys)
        print "Private keys: "
        pprint(private_keys)


def encryptionEngine(fileName, flag):
	
	encryptedFileName = fileName + ".gpg"
	print "Encrypted file name is %s" % encryptedFileName
	with open(fileName, 'rb') as fo:
	
		status = gpg.encrypt_file(fo, recipients = ['venky@fg.com'], output = encryptedFileName)

	# If debug flag is enabled, print all logs
	if flag:
		print "Status :", status.status
		print "Complete Log: ", status.stderr

	return encryptedFileName 

def decryptionEngine(fileName, flag):
	
	recoveredFileName = "recovered_" + fileName[0:(len(fileName) - 4)]
	with open(fileName, 'rb') as fo:
	
		status = gpg.decrypt_file(fo, passphrase = 'venky', output = recoveredFileName)

	# If debug flag is enabled, print all logs
        if flag:
                print "Status :", status.status
                print "Complete Log: ", status.stderr

	return recoveredFileName

def _getCurrentTime():
	return time.time()
	
def getStatistics(master_list):
	
	number_of_files = len(master_list)
	average = (sum(master_list))/number_of_files
	return average, number_of_files
	

			
def main():
	
	# Use the below condition only to generate new keys
	
	if ROOT_MODE == 1:
		key = createKey()
		exportKey(key,FILENAME)
		importKeysIntoGPG(FILENAME, False)
#	listAvailableKeys()

	if MODE == 1:
		
		
	#	importKeysIntoGPG(FILENAME, DEBUG)
		os.chdir("./")
		for file in glob.glob("*.txt"):
			encryptedFileName = encryptionEngine(file, False)
			

		#############################	
		print "Starting decryption"
		for file in glob.glob("*.txt.gpg"):
		
			timeBefore = _getCurrentTime()
			recoveredFileName = decryptionEngine(encryptedFileName, False)
			timeAfter = _getCurrentTime()
			timeDelta = timeAfter - timeBefore
			master_list.append(timeDelta)
		
		mean, number_of_files = getStatistics(master_list)
		sd = numpy.std(master_list, axis=0)
		print "Mean and Number of files and Total time is ", mean, number_of_files, mean*number_of_files
		print "Standard deviation: ", sd
	
if __name__=="__main__":
	main()

