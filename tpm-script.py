# Date : 11/06/2017
# File : tpm-script.py
# Authors : Shikha Fadnavis and Venkatesh Gopal (Johns Hopkins University, Information Security Institute)


import subprocess

def listKeys(): 
	op = subprocess.call(["gpg", "--list-keys"])
	return op


def main():
	output = listKeys()
        print output
        print type(output)
	print "hello"



if __name__ == "__main__":
	main()






