import os
import gnupg, sys
from pprint import pprint
######################

# Globally held data 
# These can be overwritten by the API
FILENAME = "mykey.asc"
PLAINTEXT_FILE = "plaintext.txt"
DEBUG = True
# Global GPG Initialization

if os.path.exists("/home/testgpguser/gpghome"):
	os.system("rm -r /home/testgpguser/gpghome")

gpg = gnupg.GPG(gnupghome="/home/testgpguser/gpghome")

# User space routines
def createKey():
        
	input_data = gpg.gen_key_input(name_email = 'venky@fg.com', passphrase = 'venky')

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

def main():
	
	key = createKey()
	exportKey(key,FILENAME)
	importKeysIntoGPG(FILENAME, DEBUG)
#	listAvailableKeys()

	encryptedFileName = encryptionEngine(PLAINTEXT_FILE, DEBUG)
	recoveredFileName = decryptionEngine(encryptedFileName, DEBUG)
	

	
if __name__ == "__main__":
        main()

