# Automatic-File-Organizer
This repository contains code which enables us to automatically move files of a given type from a tracking directory to a destination directory.

Usage: 

```
  python autoFileMove.py
```
By running the above file, it will get the input from the user for the tracking directory and the destination directory. Once the input is given and the configuration is successful, the script will keep running. When the downloaded file is a PDF, the file will be automatically moved to the destination directory. This is useful in case where we manage a separate directory for specific file types. For example, Students prefer to have their PDFs in a separate directory to manage and locate their college lectures slides easily. The type of file is customisable by altering the checking condition of the guess_type method in the mimetypes library.


