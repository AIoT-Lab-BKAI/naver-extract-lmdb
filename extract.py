# Use this file to check file lmdb
# To return images to output folder and you can check that images
import random
import sys
import os
import argparse

import lmdb 
from PIL import Image
import six
from tqdm import tqdm


parser = argparse.ArgumentParser()
parser.add_argument('--src', type=str, required=True, help='Path of lmdb folder')
parser.add_argument('--dst', type=str, required=True, help='Path of extract folder')
# parser.add_argument('--num_imgs', type=int, default=10, help='Number of required images')
args = parser.parse_args()

list_sub_dir = os.listdir(args.src)
total = 0

if not os.path.exists(args.dst):
    os.mkdir(args.dst)

label_dir = args.dst + '_label'
if not os.path.exists(label_dir):
    os.mkdir(label_dir)

for sub_dir in tqdm(list_sub_dir):

    sub_src = os.path.join(args.src, sub_dir)
    env = lmdb.open(sub_src, max_readers=32, readonly=True)
    txn = env.begin()

    nSamples = int(txn.get('num-samples'.encode()))
    total += nSamples

    index = 0
    while True:
    # for index in tqdm(range(args.num_imgs)):
        try:
            img_key = b'image-%09d' % index
            label_file = 'label-%09d'% index
            label = txn.get(label_file.encode()).decode()
            imgbuf = txn.get(img_key)
            buf = six.BytesIO()
            buf.write(imgbuf)
            buf.seek(0)
            img = Image.open(buf).convert('RGB')
            # print(label)
            img.save(os.path.join(args.dst, sub_dir + str(index) + '.png'))
            # save label of image
            filepath = os.path.join(label_dir, sub_dir + str(index) + '.txt')
            with open(filepath, 'w') as f:
                f.write(label)
            index += 1
        except:
            break

print("Number of extracted images: {}".format(total))
