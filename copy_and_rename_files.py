import shutil
import os

# Specify the paths for the source parent folder and the destination folder
parent_folder = r'D:\YOUTUBE\uload'
destination_folder = r'D:\YOUTUBE\modified'
new_extension = '.mp3'

def copy_files_to_folder(parent_folder,destination_folder):
    # Iterate through each subfolder in the parent folder
    for subfolder in os.listdir(parent_folder):
        subfolder_path = os.path.join(parent_folder, subfolder)

        # Check if the item is a directory
        if os.path.isdir(subfolder_path):
            # Get a list of files in the subfolder
            files_in_subfolder = os.listdir(subfolder_path)

            # Look for a file with the .mp4 extension
            mp4_files = [file for file in files_in_subfolder if file.lower().endswith('.mp4')]

            if mp4_files:
                # Assuming there's only one MP4 file in each subfolder
                mp4_filename = mp4_files[0]

                # Construct the source and destination file paths
                source_file_path = os.path.join(subfolder_path, mp4_filename)
                destination_file_path = os.path.join(destination_folder, f'{mp4_filename}')
                
                # Copy the MP4 file to the destination folder
                shutil.copy(source_file_path, destination_file_path)

            else:
                print(f"No MP4 file found in '{subfolder}'")


def rename_file_extension(destination_folder, new_extension):
    for filename in os.listdir(destination_folder):
        file_path = os.path.join(destination_folder, filename)

        # Check if the item is a file and has the '.mp4' extension
        if os.path.isfile(file_path) and filename.lower().endswith('.mp4'):
            # Construct the destination file path with the new extension
            base_filename , org_extension = os.path.splitext(filename)
            new_filename = f'{os.path.splitext(filename)[0]}{new_extension}'
            destination_file_path = os.path.join(destination_folder, new_filename)

            # Rename the file
            os.rename(file_path, destination_file_path)

            print(f"File '{filename}' renamed to '{new_filename}'")

    print("*************Renaming complete*****************")

# Copy MP4 files to the destination folder
copy_files_to_folder(parent_folder, destination_folder)

# Rename the copied files to have the new extension
rename_file_extension(destination_folder, new_extension)
