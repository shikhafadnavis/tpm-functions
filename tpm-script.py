# Date : 11/06/2017
# File : tpm-script.py
# Authors : Shikha Fadnavis and Venkatesh Gopal (Johns Hopkins University, Information Security Institute)


from subprocess import Popen, PIPE

# Trial function
def listKeys(): 
	op = Popen(["gpg", "--list-keys"], stdin = PIPE, stdout = PIPE)
	print ("stdout is: ", op.stdout.readlines()[2])
	print ("type of stdout is: ", type(op.stdout))
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
		


def main():
	output = listKeys()
        print output.stdout.readlines()
	generateGPGkeys()



if __name__ == "__main__":
	main()






