import os
import shutil

path_url = r"fill file location in"

extensionList = {
    "pdf": "PDF",
    "xlsx": "Excel",
    "png": "Pictures",
    "jpg": "Pictures"
}

def file_organizer(path_url):
    try:
        # Check if the directory exists
        if not os.path.exists(path_url):
            print(f"The directory {path_url} does not exists.")
            return
        
        # Change to correct directory
        os.chdir(path_url)

        #List files and directories
        files_and_directories = os.listdir()

        # Loop through all files and get the extension
        for file in files_and_directories:
            # Skip hidden files and directories
            if file.startswith("."):
                continue

            # Check if it is a file
            if os.path.isfile(file):
                #Check if file has an extension in the extensionList
                files_extension = file.split(".")[-1]
            
                if files_extension in extensionList:
                    # Create the directory if it doesn't exist
                    directory = extensionList[files_extension]
                    if not os.path.exists(directory):
                        os.makedirs(directory)
                    # Move the file to the corresponding directory
                    shutil(file, os.path.join(directory, file))
                    print(f"Moved {file} to {directory}")
                else:
                    print(f"No matching extension for {file}")
    except Exception as e:
        print(f"An error occured: {e}")

file_organizer(path_url)