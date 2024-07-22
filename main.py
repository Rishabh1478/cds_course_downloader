import os
import pandas as pd
from pathlib import Path
from downloader import downloader
import os

def download_course():
    def list_files_in_folder(folder_path):
        return [file.name for file in Path(folder_path).iterdir() if file.is_file()]

    folder_name = 'info'
    file_list = list_files_in_folder(folder_name)

    for csv_file_name in file_list:
        df = pd.read_csv(fr'{folder_name}\{csv_file_name}')
        class_name_list = df['class_names'].tolist()
        class_link_list = df['class_link'].tolist()
        if os.path.isdir(rf'downloads\{csv_file_name.replace(".csv", "")}'):
            pass
        else:
            os.makedirs(rf'downloads\{csv_file_name.replace(".csv", "")}')
        for file_name, link in zip(class_name_list, class_link_list):
            if file_name in f'{list_files_in_folder(f"downloads/{csv_file_name.replace(".csv", "")}")}':
                print('skipped')
                pass
            else:
                print(f'Downloading classes for {csv_file_name}')
                downloader(link, csv_file_name.replace('.csv', ''), file_name)
            
        