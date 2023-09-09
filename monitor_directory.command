#!/usr/bin/env python3
import os
import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory and os.path.splitext(event.src_path)[0].endswith("CV"):  # Change the file extension as needed
            subprocess.run(["bash", "/Users/josetiznado/PythonProjects/hyperlink-automation/run_script.sh"])  # Replace with the appropriate script for your OS

def monitor_directory(path):
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    directory_to_monitor = "/Users/josetiznado/Documents"
    monitor_directory(directory_to_monitor)