import os
from glob import glob
from pathlib import Path
import shutil

# Raw dataset
input_path = '../data/GEMEP_dataset/'

def copy_rename(old_file_name, new_file_name):
    src_dir = input_path
    dst_dir = '../out/video/'
    src_file = os.path.join(src_dir, old_file_name)
    shutil.copy(src_file, dst_dir)

    dst_file = os.path.join(dst_dir, old_file_name)
    new_dst_file_name = os.path.join(dst_dir, new_file_name)
    os.rename(dst_file, new_dst_file_name)


input_file_paths = glob(input_path + '*.wmv')

for path in input_file_paths:
    old_file_name = Path(path).name
    new_file_name = Path(Path(path).stem).stem + '.wmv'
    copy_rename(old_file_name, new_file_name)
