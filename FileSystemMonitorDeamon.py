import time, os, os.path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import tpm-script as tpmFunctions

#################################

masterBookKeeper = []

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
            masterBookKeeper.append([event.src_path,True])

def encryptFile(filename, emailID):
        #get public key for the user
        tpmFunctions.encryptData(filename, emailID)

def _getCurrentTime()
	return time.now()

def masterHandler()

	emailID1 = "sfad@fg.com"
        emailID2 = "vgop@fg.com"
        for i in range(0,len(masterBookKeeper)):
		if masterBookKeeper[i][1] == True:
			# Encrypting the file
			print "%s is being encrypted" %masterBookKeeper[i][0]
			timeBefore = _getCurrentTime()
			encryptFile(masterBookKeeper[i][0],emailID1)
			timeAfter = _getCurrentTime()
			deltaEncryption = timeAFter - timeBefore
			# Post encryption operation unset the modifier flag
			masterBookKeeper[i][1] = False

		else:
			print "%s is already enrypted" % masterBookKeeper[i][0]

def main():
	# Start the asycio event handler
	w = watcher()
	w.run()
	# Master Handler monitors for file changes
	masterHandler()

if __name__ == "__main__":
        main()




