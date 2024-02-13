import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class FileHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        if event.is_directory:
            return

        source_path = event.src_path
        
        # change the path to your desired location
        destination_base = "C:\\Users\\Eren\\Desktop\\Folders\\media"

        if source_path.endswith((".txt", ".md", ".doc", ".docx", ".log")):
            destination_folder = "Text"
        elif source_path.endswith((".pdf")):
            destination_folder = "PDFS"
        elif source_path.endswith((".mp4", ".webm", ".mkv")):
            destination_folder = "Videos"
        elif source_path.endswith((".jpg", ".jpeg", ".png", ".gif", ".tiff", ".tif", ".raw")):
            destination_folder = "Images"
        # skip temporary and (partial) downloading files
        elif source_path.endswith((".tmp", ".crdownload", ".ini", ".part")):
            return
        else:
            destination_folder = "Other"

        destination_path = os.path.join(destination_base, destination_folder)
        os.makedirs(destination_path, exist_ok=True)

        # If you prefer to only move (and not copy), you can delete the following if-else block and use 
        # shutil.move(source_path, destination_path)
        shutil.move(source_path, destination_path) if destination_folder == "Videos" else shutil.copy(source_path, destination_path)


def main():
    # original download location
    folder_to_watch = "C:\\Users\\Eren\\Downloads"

    event_handler = FileHandler()
    observer = Observer()
    observer.schedule(event_handler, folder_to_watch, recursive=False)  
    observer.start()

    try:
        observer.join()
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    main()
