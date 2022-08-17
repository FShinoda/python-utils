# Imports
import os
import shutil

# Vars - dinamic
diff_folder = 'C:/Users/fernanda.shinoda/Desktop/project/origin_folder/'
full_folder = 'C:/Users/fernanda.shinoda/Desktop/project/compare_folder/'
destiny_folder = 'C:/Users/fernanda.shinoda/Desktop/project/result_folder/'

# Functions
def diff_folders(diff_folder, full_folder, destiny_folder):
    """ Set B - Set A (folder_full - folder_diff)"""
    
    # Vars -fixed
    count = 0

    # Replace destiny folder
    os.rmdir(destiny_folder)
    os.mkdir(destiny_folder)

    diff_list = os.listdir(diff_folder)

    for dirpath, dirnames, files in os.walk(full_folder):
        for file in files:
            if file not in diff_list:
                print(file)
                count += 1
                shutil.copy(full_folder+file, destiny_folder)

    print(f'{count} different(s) file(s)')

# Main
diff_folders(diff_folder, full_folder, destiny_folder)
