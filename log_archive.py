"""
this script will be used to archive logs on a set schedule by compressing them
and storing them in a new directory
"""

# command to use it (provide the log directory as an argument when running the tool):
# log-archive <log-directory> >>> logs_archive_20240816_100648.tar.gz

from datetime import datetime
import tarfile
import os


now = datetime.now()
format_date = now.strftime("%Y%m%d_%H%M%S")
print(format_date)

files = ["logs"]
existing_files = [f for f in files if os.path.exists(f)]

name_tar = f'logs_archive_{format_date}.tar.gz'

# 'w:gz' opens the file for writing with gzip compression
if existing_files:
    name_tar = f'logs_archive_{format_date}.tar.gz'
    with tarfile.open(name_tar, "w:gz") as tar:
        for file in existing_files:
            tar.add(file, arcname=os.path.basename(file))
    print(f"{name_tar} was successfully created.")
else:
    print("No logs folder found. No archive was created.")
