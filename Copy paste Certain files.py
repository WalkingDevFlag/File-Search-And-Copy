import os
import shutil

def search_and_copy_files(directory, extension, destination_folder):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                file_path = os.path.join(root, file)
                shutil.copy(file_path, destination_folder)

directory = input("Enter the directory path: ")
extension = input("Enter the file extension: ")
destination_folder = input("Enter the destination folder name: ")

search_and_copy_files(directory, extension, destination_folder)
