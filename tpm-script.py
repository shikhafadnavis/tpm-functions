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


def main():
	output = listKeys()
	if (output is not None):
        	print output.stdout.readlines()



if __name__ == "__main__":
	main()






