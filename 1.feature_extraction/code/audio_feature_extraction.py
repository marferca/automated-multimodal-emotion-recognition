import os
import subprocess
from glob import glob
from pathlib import Path
from tqdm import tqdm

input_path = '../../0.preprocessing/out/audio/'
egemaps_output_path = '../out/audio/egemaps/'
gemaps_output_path = '../out/audio/gemaps/'


# openSMILE config
opensmile_path = '../../../lib/opensmile-2.3.0/'
bin_path = os.path.join(opensmile_path, 'inst', 'bin')
egemaps_conf_file_path = os.path.join(opensmile_path, 'config', 'gemaps', 'eGeMAPSv01a.conf')
gemaps_conf_file_path = os.path.join(opensmile_path, 'config', 'gemaps', 'GeMAPSv01a.conf')


input_file_paths = glob(input_path + '*.wav')

for file_path in tqdm(input_file_paths):
    #print(file_path)
    subprocess.call([bin_path + '/SMILExtract',
                    '-C', egemaps_conf_file_path,
                    '-I', file_path,
                    '-O', egemaps_output_path + 'egemaps_' + Path(file_path).stem + '.csv'
                    ],stderr=subprocess.DEVNULL
                   )

    subprocess.call([bin_path + '/SMILExtract',
                    '-C', gemaps_conf_file_path,
                    '-I', file_path,
                    '-O', gemaps_output_path + 'gemaps_' + Path(file_path).stem + '.csv'
                    ],stderr=subprocess.DEVNULL)
