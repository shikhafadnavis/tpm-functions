# Date : 12/10/2017
# File : tpm_script_encrypt.py {For performance testing of file encryption using GPG keys}
# Authors : Shikha Fadnavis and Venkatesh Gopal (Johns Hopkins University, Information Security Institute)


from subprocess import Popen, PIPE
import os.path
import os
import getpass
import random, string, gnupg

def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))


def listKeys(): 
	
	os.system("gpg --list-keys")

def generateGPGkeys():
	# generate randomness
	Popen(["sudo", "rngd", "-r", "/dev/urandom"])

	# generate GPG keys
	cmd = "gpg --gen-key"
	os.system(cmd)

def encryptData(filename, EmailID):
	
	op = Popen(["gpg", "--encrypt", "--recipient", "--trust-model", "always", EmailID, filename], stdin=PIPE, stdout=PIPE, universal_newlines=True)

	if(op.stdout):
		for line in op.stdout:
			if line.startswith("Use this key anyway?"):
				answer = y	

			print(answer, op.stdin)
			op.stdin.flush()

def decryptData(encryptedFileName):

	gpg = gnupg.GPG(homedir='/home/sfubuntu1422/tpm-functions')
	gpg.encoding = 'utf-8'
	unsealedPrivateKeyFileName = raw_input("\n Enter the name of your unsealed private key file \n")
	recoveredFilename = encryptedFileName + "recovered"
	cmd = "gpg --import " + unsealedPrivateKeyFileName
	os.system(cmd)	
#	password = getpass.getpass()
#	op = Popen(["gpg","--passphrase","venky","-q", "--output", recoveredFilename, "--decrypt", encryptedFileName])
	decrypted_data = gpg.decrypt_file(encryptedFileName)
	print type(decrypted_data)


def encryptPrivateKeysUsingTPM(Identity,EmailID):

	userPublicKeyFileNameHelper = EmailID + "_publickey.asc"
	userPrivateKeyFileNameHelper = EmailID + "_privatekey.asc"
	userEncryptedPrivateKeyFileNameHelper = EmailID + "_keyblob"

	# Calling helper functions to Export keys into GPG before sealing them
	_helper_ExportPrivateKey(Identity,userPrivateKeyFileNameHelper)
	_helper_ExportPublicKey(EmailID,userPublicKeyFileNameHelper)

	# Sealing the private key using the TPM secret key
	cmd = "tpm_sealdata --infile " + userPrivateKeyFileNameHelper + " --outfile " + userEncryptedPrivateKeyFileNameHelper + " --pcr 0 --pcr 7"
	os.system(cmd)

	# Delete private key from gpg
	cmd = "gpg --delete-secret-keys " + EmailID
	os.system(cmd)

	#Delete public key from gpg
	cmd = "gpg --delete-keys " + EmailID
	os.system(cmd)

	# Removing the private key file from the system
	cmd = "rm " +  userPrivateKeyFileNameHelper
	os.system(cmd)
	
	return userEncryptedPrivateKeyFileNameHelper
	
def _helper_ExportPrivateKey(Identity,userPrivateKeyFileNameHelper):

	cmd = "gpg " + "--export-secret-keys -a " + Identity + " > " + userPrivateKeyFileNameHelper
	os.system(cmd)

def _helper_ExportPublicKey(EmailID,userPublicKeyFileNameHelper):
	
	cmd = "gpg --armor --export " + EmailID + " > " + userPublicKeyFileNameHelper
	os.system(cmd)

def decryptPrivateKeyUsingTPM(fileName_keyblob):

	outputFileName = randomword(10) + "_unsealedPrivate.key"
	cmd = "tpm_unsealdata --infile " + fileName_keyblob + " --outfile " + outputFileName
	os.system(cmd)

	return outputFileName

'''def main():
	print "Please select one of the following choices: "
	print "1. List available GPG keys \n2. Generate GPG Keys \n3. Encrypt data \n4. Decrypt data \n5. Encrypt Private keys using key in the TPM \n6. Decrypt the private key using the key on the TPM \n"

	choice  = raw_input("Enter your choice here: ")

	if choice == '1':
		listKeys()
	elif choice == '2':
		generateGPGkeys()
	elif choice == '3':
		filename = raw_input("\nEnter the name of the file to be encrypted\n")
		EmailID = raw_input("\nEnter the Email ID\n")
		
		if os.path.isfile(filename):
			encryptData(filename,EmailID)
		else:
			print "File not found!"
			 
	elif choice == '4':
		encryptedFileName = raw_input("\nEnter the encrypted file name\n")
		decryptData(encryptedFileName)

	elif choice == '5':
		Identity = raw_input("\nEnter the identity for the public key generation\n")
		# We need to put checks if the Email ID's and filename's exist
                # Have to figure out a way for that
		EmailID = raw_input("\nEnter the Email ID\n")
		
		encryptedFileName = encryptPrivateKeysUsingTPM(Identity,EmailID)
		print "Operation Success, Your Encrypted Private Key file name is: ", encryptedFileName," \n"

	elif choice == '6':
		fileName = raw_input("\nEnter the name of your encrypted private key ")
		outputFileName = decryptPrivateKeyUsingTPM(fileName)
		print " Your decrypted private key file name is : ", outputFileName
	else:
		print "Wrong Choice" 




if __name__ == "__main__":
	main()


'''



