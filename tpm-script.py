# Date : 11/06/2017
# File : tpm-script.py
# Authors : Shikha Fadnavis and Venkatesh Gopal (Johns Hopkins University, Information Security Institute)


from subprocess import Popen, PIPE
import os.path
import getpass
import random, string

def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))


def listKeys(): 
	op = Popen(["gpg", "--list-keys"], stdin = PIPE, stdout = PIPE)
	print op.stdout.readlines()
	#print ("stdout is: ", op.stdout.readlines()[2])
	#print ("type of stdout is: ", type(op.stdout))
	return op

def generateGPGkeys():
	# generate randomness
	Popen(["sudo", "rngd", "-r", "/dev/urandom"])

	# generate GPG keys
	op = Popen(["gpg2", "--gen-key"], stdin=PIPE, stdout=PIPE, universal_newlines=True)
	for line in op.stdout:
		if line.startswith("Your selection?"):
			answer = 1
		elif line.startswith("What keysize do you want?"):
			answer = 2048
		elif line.startswith("Key is valid for?"):
			answer = 0
		elif line.startswith("Is this correct?"):
			answer = y 
		else:
			break

		print(answer, op.stdin)
		op.stdin.flush()

def encryptData(filename):
	op = Popen(["gpg", "--encrypt", "--recipient", "sfadnav1@jhu.edu", filename], stdin=PIPE, stdout=PIPE, universal_newlines=True)

#	op = Popen(["gpg2", "--encrypt", "--recipient", "sfad@jh.edu", filename], stdin=PIPE, stdout=PIPE, universal_newlines=True)

	for line in op.stdout:
		if line.startswith("Use this key anyway?"):
			answer = y	

	print(answer, op.stdin)
	op.stdin.flush()

def decryptData():
#	password = raw_input("Enter the password to your private key")
	password = getpass.getpass()
	op = Popen(["gpg","--passphrase", password, "--decrypt", "plaintext2.txt.gpg"])


def encryptPrivateKeysUsingTPM(Identity,EmailID):

	userPublicKeyFileNameHelper = EmailID + "_publickey.asc"
	userPrivateKeyFileNameHelper = EmailID + "privatekey.asc"
	userEncryptedPrivateKeyFileNameHelper = EmaildID + "_keyblob"

	_helper_ExportPrivateKey(Identity,userPrivateKeyFileNameHelper)
	_helper_ExportPublicKey(EmailID,userPublicKeyFileNameHelper)

	op = Popen(["tpm_sealdata", "--infile", userPrivateKeyFileNameHelper, "--outfile",userEncryptedPrivateKeyFileNameHelper, "--pcr", "0", "--pcr", "7"], stdin=PIPE, stdout=PIPE,universal_newlines=True)

	return userEncryptedPrivateKetFileNameHelper
	
def _helper_ExportPrivateKey(Identity,userPrivateKeyFileNameHelper):

	op = Popen(["gpg", "--export-secret-keys", "-a", Identity, ">", userPrivateKeyFileNameHelper])

def _helper_ExportPublicKey(EmailID,userPublicKeyFileNameHelper):
	
	op = Popen(["gpg", "--armor", "--export", EmailID, ">",userPublicKeyFileNameHelper])

def decryptPrivateKeyUsingTPM(fileName_keyblob):

	outputFileName = randomword(10) + "_unsealedPrivate.key"

	op = Popen(["tpm_unsealdata", "--infile", fileName_keyblob, "--outfile", outputFileName], stdin=PIPE, stdout=PIPE, universal_newlines=True)

	return outputFileName

def main():
	print "Please select one of the following choices: "
	print "1. List available GPG keys \n2. Generate GPG Keys \n3. Encrypt data \n4. Decrypt data \n 5. Encrypt Private keys using key in the TPM \n "
	"6. Decrypt the private key using the key on the TPM \n"
	choice  = raw_input("Enter your choice here: ")

	if choice == '1':
		listKeys()
	elif choice == '2':
		generateGPGkeys()
	elif choice == '3':
		filename = raw_input("Enter the name of the file to be encrypted")
		if os.path.isfile(filename):
			encryptData(filename)
		else:
			print "File not found!"
			 
	elif choice == '4':
		decryptData()
	elif choice == '5':
		Identity = raw_input("\nEnter the identity for the public key generation\n")
		# We need to put checks if the Email ID's and filename's exist
                # Have to figure out a way for that
		EmailID = raw_input("\nEnter the Email ID\n")
		
		encryptedFileName = encryptPrivateKeysUsingTPM(Identity,EmailID)
		print "Operation Success, Your Encrypted Private Key file name is: ", encryptedFileName," \n"

	elif choice == '6':
		fileName = raw_input("\n Enter the name of your encrypted private key ")
		outputFileName = decryptPrivateKeyUsingTPM(fileName)
		print " Your decrypted private key file name is : ", outputFileName
	else:
		print "Wrong Choice" 




if __name__ == "__main__":
	main()






