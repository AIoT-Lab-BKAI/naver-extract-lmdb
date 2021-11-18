## Prerequisites
- Python 3

## Installation
```bash
git clone https://github.com/AIoT-Lab-BKAI/naver-extract-lmdb
cd naver-extract-lmdb
```

### Create new python virtual environments
```bash
python -m venv ./naver-extract-lmdb
source ./naver-extract-lmdb/bin/activate
pip install -r requirements.txt
```

### How to use
```bash
python extract.py --src PATH_TO_LMDB_FOLDER --dst PATH_TO_SAVE_FOLDER
```
- We specified path to LMDB folders in attached docs [here](https://docs.google.com/document/d/1LJGBUyaMGCErbZcS2aOcZptwKKvYHtrBCeUg9-EnxiU/edit?usp=sharing)
- For example, if you want to extract '/mnt/disk2/baoanh/SCAN-UNIGRAM-MULTIPROCESS-FIRST-45M/train_ocr' folder into 'unigram_images' folder, use this command:
```bash
python extract.py --src /mnt/disk2/baoanh/SCAN-UNIGRAM-MULTIPROCESS-FIRST-45M/train_ocr --dst unigram_images

```
- After running, it will save all the raw images into 'unigram_images' folder and corresponding labels for each raw image in 'unigram_images_label' folder

### Results
- Raw images folder (E.g. 'unigram_images' folder)
- Label folder with corresponding label for each image in images folder (E.g. 'unigram_images_label' folder)

### Notes
- It may take some times to extract large folder (e.g. To extract 1.9GB folder, it took ~20 minutes)

### Contact
Email: anh.pnb176682@sis.hust.edu.vn