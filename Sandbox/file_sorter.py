"""
sorts files
"""
import os
import shutil

FILE_LOCATION = input("Please input the folder location you would like to organize: ")

mapping = {
            '.epub': 'Books',
            '.zip': 'Compressed Files',
            '.cbz': 'Comics',
            '.pdf': 'Documents',
            '.csv': 'Documents',
            '.doc': 'Documents',
            '.docx': 'Documents',
            '.jpg': 'Images',
            '.png': 'Images',
            '.mp3': 'Music',
            '.mp4': 'Videos',
            '.mkv': 'Videos',
            '.avi': 'Videos',
            '.ini': 'Other'
}

if FILE_LOCATION == '':
    FILE_LOCATION = 'C:\\users\\bcrob\\Downloads'

# Open folder location from file_location
os.chdir(FILE_LOCATION)

def migrate_file(to_check, subdir):
    """
    move file
    """
    FOUND_EXTENSION = False
    for extension, extension_folder in mapping.items():
        if extension in to_check:
            # If it finds a mapping and no folder with the value is created create a
            # folder at this top level, i.e. if it finds a pdf and no documents
            # folder exists create one
            destination_folder = os.path.join(FILE_LOCATION, extension_folder, subdir)
            if not os.path.isdir(destination_folder):
                os.makedirs(destination_folder)

            print(f'File {to_check} is processed into: {destination_folder}')
            shutil.copy2(to_check, destination_folder)
            FOUND_EXTENSION = True
    if FOUND_EXTENSION is False:
        destination_folder = os.path.join(FILE_LOCATION, 'Other', subdir)
        if not os.path.isdir(destination_folder):
            os.makedirs(destination_folder)

        print(f'File {to_check} is processed into: Other')
        shutil.copy2(to_check, destination_folder)
    FOUND_EXTENSION = False

def migrate_folder(to_check, subdir=''):
    """
    moves down a folder then creates a backup if found of each file based upon
    mapping types.  This backs up each file but also keeps the folder structure
    into the newly created directories made in migrate_file
    """
    if to_check in mapping.values() or to_check=='Other':
        return

    os.chdir(to_check)
    for item in os.listdir():
        if os.path.isfile(item):
            migrate_file(item, subdir)
        elif os.path.isdir(item):
            migrate_folder(item, os.path.join(subdir, item))
    os.chdir('..')

print(f'Beginning processing of {FILE_LOCATION}')

for to_check in os.listdir():
    # Check each file in this location based upon mapping
    if os.path.isfile(to_check):
        migrate_file(to_check, '')
    elif os.path.isdir(to_check):
        migrate_folder(to_check, to_check)

print(f'All files have been processed at {FILE_LOCATION}')
