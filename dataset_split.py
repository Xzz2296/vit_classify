from pathlib import Path
import random
from sklearn.model_selection import train_test_split
data_dir =r'C:\xpj\UNIPUS\OCR\ocrdataset\relevant_dataset'
data_dir = Path(data_dir)

# Get the list of all files in directory tree at given path
list_of_files = list(data_dir.glob('**/*.jpg'))
keys = [file.stem for file in list_of_files]
# 去除以pdf结尾的文件
keys = [key for key in keys if not key.endswith('pdf')]
# 将key 按照8：2划分为train ,val 两部分
train_ratio = 0.7
val_ratio = 0.3

# 使用 train_test_split 函数划分数据集
keys_train, keys_val = train_test_split(keys, test_size=val_ratio)

# 将划分好的数据集保存到文件中
with open('train.txt', 'w') as f:
    f.write('\n'.join(keys_train))

with open('val.txt', 'w') as f:
    f.write('\n'.join(keys_val))

print('hello')

