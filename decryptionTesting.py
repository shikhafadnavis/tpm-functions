import os, time
import gnupg, sys
from pprint import pprint
import glob
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
######################

# Globally held data 
# These can be overwritten by the API
FILENAME = "mykey.asc"
PLAINTEXT_FILE = "plaintext.txt"
DEBUG = True
# TODO - Change the monitoring directory name
MONITORING_DIRECTORY = "/mnt/mfschunks2/00"
master_list = []
# MODE = 1 for encryption and 2 for decryption
ROOT_MODE = 1
MODE = 0
ROOT_DIRECTORY_V = "/home/venky/dummy"
ROOT_DIRECTORY_S = "/home/sfubuntu1422/mfsdummy"

# Global GPG Initialization

if os.path.exists("/home/sfubuntu/gpghome"):
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
	
class Watcher:
    DIRECTORY_TO_WATCH = "/mnt/mfschunks2/00"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print "Error"

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
	encryption_counter = 0
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Take any action here when a file is first created.
            # True indicates that the file is yet to be processed by the Encryption Engine
            #print "Event received for file %s" % event.src_path
	    cmd = "cp " + event.src_path + space + ROOT_DIRECTORY_S
            #print "Finished copying"
            filename = _extractFileName(event.src_path)
            realFilename = ROOT_DIRECTORY_S + "/" + filename
            os.system(cmd)
            cencryptedFileName = encryptionEngine(realFilename, DEBUG)
            

			
def main():
	
	# Use the below condition only to generate new keys
	
	if ROOT_MODE == 1:
		key = createKey()
		exportKey(key,FILENAME)
		importKeysIntoGPG(FILENAME, DEBUG)
#	listAvailableKeys()

	#encryptedFileName = encryptionEngine(PLAINTEXT_FILE, DEBUG)
	# TODO - Change the monitoring directory name
	if MODE == 1:
		
		w = Watcher()
		w.run()
		
	if MODE == 2:
		os.chdir(ROOT_DIRECTORY_S)
		for file in glob.glob(".gpg"):
			
			timeBefore = _getCurrentTime()
			recoveredFileName = decryptionEngine(encryptedFileName, DEBUG)
			timeAfter = _getCurrentTime()
			timeDelta = timeAfter - timeBefore
			master_list.append(timeDelta)
		
		mean, number_of_files = getStatistics(master_list)
	
if __name__=="__main__":
	main()

