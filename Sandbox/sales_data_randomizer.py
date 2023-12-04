"""
Sales data randomizer assignment
"""
import csv
import logging
import time
import random
import shutil
import sys

def setup_logger():
    """
    Sets up the logger
    """
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

def shuffle_csv(csv_to_shuffle):
    """
    Shuffles the CSV file that is given for data concerns
    """
    print('Shuffling CSV')
    random.shuffle(csv_to_shuffle)
    print('CSV Shuffled')
    return csv_to_shuffle

def save_csv(location_to_save, csv_to_save):
    """
    Saves the CSV file to the desired location with a new name
    """
    print('Saving CSV')
    with open(location_to_save, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        for csv_row in csv_to_save:
            csv_writer.writerow(csv_row)
    print('CSV Saved')

def randomizer():
    """
    Ranodmizes the data and saves to a new file
    """
    with open(ORIGINAL_CSV, newline='', encoding='utf-8') as csvfile:
        # Read CSV file and save the header
        csv_data = csv.reader(csvfile, delimiter=',')
        csv_header = next(csv_data)

        # Convert CSV to a list
        csv_list = []
        for row in csv_data:
            csv_list.append(row)

        # Shuffle the CSV file for security
        csv_list = shuffle_csv(csv_list)

        csv_list.insert(0, csv_header)

        save_csv(DESTINATION_CSV, csv_list)

setup_logger()

# Defaults
SHUFFLE_TIME = 15
ORIGINAL_CSV = './Sandbox/sales_data/sales_data.csv'
CURRENT_TIME = str(time.time())
DESTINATION_CSV = f'./Sandbox/sales_data/sales_data{CURRENT_TIME}.csv'



file_loc = input('Which file would you like to use? (Default: sales_data.csv)\n')

if file_loc != '':
    ORIGINAL_CSV = ORIGINAL_CSV.replace('sales_data.csv', file_loc)

shutil.copyfile(ORIGINAL_CSV, DESTINATION_CSV)

time_delay = int(input(f'How long would you like to wait before shuffling the CSV file? (Default: {SHUFFLE_TIME})\n'))
shuffle_times = int(input('How many times would you like to shuffle the CSV file?\n'))

if time_delay == '':
    time_delay = SHUFFLE_TIME
if shuffle_times == '':
    shuffle_times = 1

for i in range(shuffle_times):
    try:
        randomizer()
        time.sleep(time_delay)
        LOG_TIME = str(time.time())
        logging.debug(f'CSV Shuffled {i+1} times\n')
        logging.debug(f'Shuffled at {LOG_TIME}\n')
    except KeyboardInterrupt:
        print('Keyboard Interrupt detected. Exiting...')
        break
