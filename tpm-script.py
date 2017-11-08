# Date : 11/06/2017
# File : tpm-script.py
# Authors : Shikha Fadnavis and Venkatesh Gopal (Johns Hopkins University, Information Security Institute)


from subprocess import Popen, PIPE


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
	op = Popen(["gpg", "--gen-key"], stdin=PIPE, stdout=PIPE, universal_newlines=True)
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

def encryptData():
	op = Popen(["gpg", "--encrypt", "--recipient", "sfadnav1@jhu.edu", "plaintext.txt"], stdin=PIPE, stdout=PIPE, universal_newlines=True)
	for line in op.stdout:
		if line.startswith("Use this key anyway?"):
			answer = y	

	print(answer, op.stdin)
	op.stdin.flush()

def decryptData():
	op = Popen(["gpg", "--decrypt", "plaintext.txt.gpg"])

def encryptPrivateKeysUsingTPM():
	_helper_ExportPrivateKey()
	_helper_ExportPublicKey()

	op = Popen(["tpm_sealdata", "--infile", "privateKet.asc", "--outfile","keyblob", "--pcr", "0", "--pcr", "7"], stdin=PIPE, stdout=PIPE,universal_newlines=True)
	
def _helper_ExportPrivateKey():

	op = Popen(["gpg", "--export-secret-keys", "-a", "1E2214B6", ">", "privatekey.asc"])

def _helper_ExportPublicKey():
	
	op = Popen(["gpg", "--armor", "--export", "venky@venky", ">", "publicKey.asc"])

def decryptPrivateKeyUsingTPM():

	op = Popen(["tpm_unsealdata", "--infile", "keyblob", "--outfile", "unseadledPrivate.key"], stdin=PIPE, stdout=PIPE, universal_newlines=True)

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
		encryptData() 
	elif choice == '4':
		decryptData()
	elif choice == '5':
		encryptPrivateKeysUsingTPM()
	elif choice == '6':
		decryptPrivateKeyUsingTPM()
	else:
		print "Wrong Choice" 




if __name__ == "__main__":
	main()






