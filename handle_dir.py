import os
import codecs
from tqdm import tqdm

def handle_directory(dir, new_file=None):
    total_sents = []
    fnames = os.listdir(dir)
    for i in tqdm(fnames):
        fpath = os.path.join(dir, i)
        if os.path.isfile(fpath):
            lines = codecs.open(fpath, 'r', 'utf-8').readlines()
            for line in lines:
                line = line.strip()
                total_sents.append(line)
    new_file = open(new_file, 'w')
    for i in total_sents:
        new_file.write(i)
        new_file.write('\n')
    new_file.close()

# if __name__ == '__main__':
#     dir = '/ssd3/exec/wangchf/data/en_single_data/en-US-Wavenet-D/txts'
#     new_file = './en-US-Wavenet-D.txt'
#     handle_directory(dir=dir, new_file=new_file)
