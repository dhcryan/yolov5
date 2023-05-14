import os
import random
import shutil

# 이미지 파일이 있는 폴더 경로
img_folder = 'C:\\Users\\dhc40\\vision\\23_ML\\yolov5\\data2\\images'

# train, test, val 폴더 생성
os.makedirs(os.path.join(img_folder, 'train'), exist_ok=True)
os.makedirs(os.path.join(img_folder, 'test'), exist_ok=True)
os.makedirs(os.path.join(img_folder, 'val'), exist_ok=True)

# 클래스 별 이미지 파일 리스트 생성
class0_imgs = []
class1_imgs = []
for file_name in os.listdir(img_folder):
    if file_name.endswith('.jpg'):
        if random.random() < 0.8:
            shutil.move(os.path.join(img_folder, file_name), os.path.join(img_folder, 'train', file_name))
        elif random.random() < 0.9:
            shutil.move(os.path.join(img_folder, file_name), os.path.join(img_folder, 'val', file_name))
        else:
            shutil.move(os.path.join(img_folder, file_name), os.path.join(img_folder, 'test', file_name))
