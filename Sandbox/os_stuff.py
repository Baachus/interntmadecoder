"""
This file demonstrates some of the basic functions of the os module.
"""
import os

# Getting the current working directory
current_directory = os.getcwd()
print('Current Working Directory: ', current_directory)

# Listing files in the current directory
files = os.listdir()
print('Files in the Current Directory: ', files)

# Creating a new directory
os.mkdir('new_directory')
print('Created new directory: new_directory')

# Removing a directory
os.rmdir('new_directory')
print('Removed new directory: new_directory')
