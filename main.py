import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from config import WATCHED_FOLDER
from file_sorter import move_file

class FileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            time.sleep(1)  # Warten, bis Datei komplett geladen ist
            move_file(event.src_path)

if __name__ == "__main__":
    print(f"📂 Überwache Ordner: {WATCHED_FOLDER}")
    event_handler = FileHandler()
    observer = Observer()
    observer.schedule(event_handler, WATCHED_FOLDER, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
