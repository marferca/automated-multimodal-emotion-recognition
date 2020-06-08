import os
import subprocess
from glob import glob
from pathlib import Path
from tqdm import tqdm
import shutil

input_path = '../../0.preprocessing/out/video/'
output_path = '../out/video/'
openface_path = '../../../lib/OpenFace-master/build/bin/FeatureExtraction'

input_file_paths = glob(input_path + '*.wmv')

for file_path in tqdm(input_file_paths):
    #print(file_path)
    subprocess.call([openface_path,
                     '-f', file_path,
                     '-out_dir', os.path.join(output_path, 'all')
                    ],stdout=subprocess.DEVNULL
                    )

# Copy all csv features to another directory
csv_file_paths = glob(os.path.join(output_path,'all','*.csv'))
for org_file in tqdm(csv_file_paths):
    dst_file = os.path.join(output_path, 'csv', Path(org_file).name)
    shutil.copy(org_file, dst_file)
