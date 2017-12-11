import time, os, os.path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import tpm_script_encrypt as tpmFunctions

#################################

# Holding Global variable here
emailID1 = "sfad@fg.com"
emailID2 = "vgop@fg.com"
rootDirectory = "/home/sfubuntu1422/mfsdummy"
space = " "
timeList = []

#################################
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
	    cmd = "cp " + event.src_path + space + rootDirectory
            #print "Finished copying"
            filename = _extractFileName(event.src_path)
            realFilename = rootDirectory + "/" + filename
            os.system(cmd)
            masterHandler(realFilename)

def encryptFile(filename, emailID):
        
	#get public key for the user
        tpmFunctions.encryptData(filename, emailID)

def _getCurrentTime():
	return time.time()

def _extractFileName(filename):
	
	fileAll = filename.split("/")
       	filename = fileAll[len(fileAll) - 1]
	return filename

def enigmaEngine(filename):
	#print "Time list until now:"
	#print timeList
	emailID1 = "sfad@fg.com"
        emailID2 = "venky@fg.com"
        timeBefore = _getCurrentTime()
        encryptFile(filename,emailID2)
        timeAfter = _getCurrentTime()
        deltaEncryption = timeAfter - timeBefore
	timeList.append(deltaEncryption)
        print "Operation for file %s took time %s ", filename, deltaEncryption

def masterHandler(filename):

	enigmaEngine(filename)	

def main():
	# Start the asyncio event handler
	w = Watcher()
	w.run()
	#print "Final time list is: ", timeList
	timeAvg = sum(timeList)/len(timeList)
	print "Length of timelist is: ", len(timeList)
	print "Average time for encryption is: ", timeAvg
	

if __name__ == "__main__":
        main()




