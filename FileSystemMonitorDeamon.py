import time, os, os.path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import tpm_script as tpmFunctions

#################################
# Holding Global variable here
emailID1 = "sfad@fg.com"
emailID2 = "vgop@fg.com"

class Watcher:
    DIRECTORY_TO_WATCH = "/home/sfubuntu"

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
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Take any action here when a file is first created.
            # True indicates that the file is yet to be processed by the Encryption Engine
            masterHandler(event.src_path)

def encryptFile(filename, emailID):
        
	#get public key for the user
        tpmFunctions.encryptData(filename, emailID)

def _getCurrentTime():
	return time.now()

def _extractFileName(filename):
	
	fileAll = filename.split("/")
       	filename = fileAll[2]
	return filename

def enigmaEngine(filename):

	emailID1 = "sfad@fg.com"
        emailID2 = "vgop@fg.com"
        filename = _extractFileName(filename)
        timeBefore = _getCurrentTime()
        encryptFile(filename,emailID1)
        timeAfter = _getCurrentTime()
        deltaEncryption = timeAfter - timeBefore
        print"Operation took time - ", deltaEncryption

def masterHandler(filename):

	enigmaEngine(filename)	

def main():
	# Start the asycio event handler
	w = Watcher()
	w.run()

if __name__ == "__main__":
        main()




