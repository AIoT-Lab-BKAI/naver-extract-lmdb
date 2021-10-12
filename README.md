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

### Notes
- It may take some times to extract large folder (e.g. To extract 1.9GB folder, it took ~20 minutes)