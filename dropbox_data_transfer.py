import os, shutil
from datetime import datetime, timedelta
import traceback
import xml.etree.ElementTree as ET
import logging


logging.basicConfig(filename='dropbox_log.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
# GET INPUT and OUTPUT FILE PATHS FROM XML FILE
path_file = ET.parse('data_sync.xml')
root = path_file.getroot()
INPUT_PATH = root[0].text
OUTPUT_PATH = root[1].text

def get_date_yesterday():
    today_date = datetime.now()
    yesterday = today_date - timedelta(1)
    return yesterday.strftime('%Y%m%d')

YSTRDATE = get_date_yesterday()

# RAW_IMAGES_SOURCE_DATEWISE = "/home/insightzz-08/Desktop/Navneet/DPC/DPC-Balaji/Data/InferencedImages/" 
RAW_IMAGES_SOURCE_DATEWISE = os.path.join(INPUT_PATH, YSTRDATE)
print("RAW_IMAGES_SOURCE_DATEWISE", RAW_IMAGES_SOURCE_DATEWISE)

# DESTINATION DROPBOX FOLDER 
DROPBOX_ROOT_FOLDER = os.path.join(OUTPUT_PATH, YSTRDATE)
print(DROPBOX_ROOT_FOLDER)


# Copy the directory
try:
    shutil.copytree(RAW_IMAGES_SOURCE_DATEWISE, DROPBOX_ROOT_FOLDER)
    print(f"Directory copied successfully from {RAW_IMAGES_SOURCE_DATEWISE} to {DROPBOX_ROOT_FOLDER}")
except FileExistsError:
    traceback.print_exc()
    # logging.error(f"Error: {e}")
    # print(f"Destination directory {DROPBOX_ROOT_FOLDER} already exists")
except Exception as e:
    traceback.print_exc()
    logging.error(f"Error: {e}")
    # print(f"An error occurred while copying the directory: {e}")



# 5 0 * * * /usr/bin/python3 /path/to/your_script.py >> /path/to/your_log_file.log 2>&1