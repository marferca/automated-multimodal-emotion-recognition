import os
import subprocess
from glob import glob
from pathlib import Path
from tqdm import tqdm

# Raw dataset
input_path = '../data/GEMEP_dataset/'

# Audio output
output_path = '../out/audio/'
input_file_paths = glob(input_path + '*.wmv')

for path in tqdm(input_file_paths):
    subprocess.call(['ffmpeg', '-y', '-i', path,
     output_path + Path(Path(path).stem).stem +'.wav'], stderr=subprocess.DEVNULL)
