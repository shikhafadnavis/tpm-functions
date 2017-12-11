# Date : 12/10/2017
# File : fileCreationAutomator.py{For creating files on the fly}
# Authors : Shikha Fadnavis and Venkatesh Gopal (Johns Hopkins University, Information Security Institute)

import sys, random, string, os

USAGE = """python fileCreationAutomator.py -directory=<root directory name> -c=<number of files to be created>"""

def _randomCharacterGenerator():
	random_val = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])
	return random_val
	
def main():
    Args = {}
    
    # default directory if not provided by the user
    directory = "./"
    # default count will be 1 if not provided by the user
    count = 1

    args= sys.argv[1:]
    i = 0
    for arg in args:

        if arg.startswith("-"):

            k,v = arg.split("=")
            Args[k]=v

        else:

            Args[i] = arg
            i+=1
            
    if "-directory" in Args:
        directory = Args["-directory"]

    if not os.path.isdir(directory):
	sys.exit(USAGE)

    if "-c" in Args:
	count = int(Args["-c"])
	if count > 1000 :
		sys.exit("Number of files should be less than or equal to 1000")
   
    print "Count = ", count, " and directory is ", directory 

    for i in range(0,count):
	fileName = "tester12_file_" + str(i)
	print "Processing file %s" % fileName
	fileName = directory + "/" + fileName
	createFiles(fileName)

def createFiles(fileName):

	with open(fileName, 'wb') as fout:
		fout.write(_randomCharacterGenerator())

if __name__=="__main__":
	main()
