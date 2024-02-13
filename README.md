#File Organizer Script
This Python script is designed to organize files in a specified folder based on their file types. It utilizes the watchdog library to monitor changes in a designated folder and automatically categorizes files into specific subfolders.

##Usage
###Dependencies

Ensure that you have the required dependencies installed. You can install them using the following:
```
pip install watchdog
```
###Configuration

Modify the folder_to_watch variable in the main() function to specify the folder you want to monitor. Default is "C:\Users\Eren\Downloads".

Adjust the destination_base variable in the FileHandler class to set the base directory where categorized folders will be created. Default is "C:\Users\Eren\Desktop\Folders\media".

###File Categorization

The script categorizes files into different folders based on their extensions. You can customize or expand the categories in the on_any_event method of the FileHandler class.
###Run the Script

Execute the script, and it will start monitoring the specified folder.
```
python main.py
```
###Interrupt the Script

To stop the script, press Ctrl + C.
##Supported File Types
Text Files: .txt, .md, .doc, .docx, .log
PDF Files: .pdf
Video Files: .mp4, .webm, .mkv
Image Files: .jpg, .jpeg, .png, .gif, .tiff, .tif, .raw
Other Files: All other file types
##Notes
Temporary and downloading files with extensions .tmp, .crdownload, .ini, .part are skipped.

Videos are moved, while other files are copied to their respective folders. You can adjust this behavior by modifying the script.

Make sure to handle large files and directories responsibly, as the script performs file operations.

Customize the script according to your preferences by modifying the variables and file categorization logic.
