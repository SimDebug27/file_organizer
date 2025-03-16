import os
import shutil

# Replace with the actual path to your Downloads folder
path_url = r"Downloads folder"

# Replace with the actual path to your Documents folder
folder_path = r"Documents folder"

extensionList = {
    "Documents": ["pdf", "docx", "txt", "xlsx"],
    "Pictures": ["png", "jpg", "jpeg"],
    "Games": ["zip"]
}

def file_organizer(path_url, folder_path):
    try:
        # Check if the downloads exists
        if not os.path.exists(path_url):
            print(f"The directory {path_url} does not exists.")
            return
        
        # Check if the documents exists
        if not os.path.exists(folder_path):
            print(f"The directory {folder_path} does not exists.")
            return

        #List files and directories
        files_and_directories = os.listdir(path_url)

        # Loop through all files and get the extension
        for file in files_and_directories:
            # Skip hidden files and directories
            if file.startswith("."):
                continue

            # Check if it is a file
            # Full path to the file
            file_path = os.path.join(path_url, file)
            if os.path.isfile(file_path):
                #Check if file has an extension in the extensionList
                files_extension = file.split(".")[-1]

                # Find the corresponding folder for the extension
                folder_found = False
                for folder, extensions in extensionList.items():
                    if files_extension in extensions:
                        # Create the directory in Documents if it doesn't exist
                        target_folder = os.path.join(folder_path, folder)
                        if not os.path.exists(target_folder):
                            os.makedirs(target_folder)

                        # Move the file to the corresponding directory
                        shutil.move(file_path, os.path.join(target_folder, file))
                        print(f"Moved {file} to {target_folder}")
                        folder_found = True
                        break
                else:
                    print(f"No matching extension for {file}")
    except Exception as e:
        print(f"An error occured: {e}")

file_organizer(path_url, folder_path)