import os
import random
from sklearn.model_selection import train_test_split
import shutil

# 이미지와 라벨 데이터의 경로
images_path = r"C:\Users\dhc40\vision\23_ML\yolov5\data4\images"
labels_path = r"C:\Users\dhc40\vision\23_ML\yolov5\data4\labels"

# train, val 데이터를 저장할 경로
train_images_path = os.path.join(images_path, "train")
val_images_path = os.path.join(images_path, "val")
train_labels_path = os.path.join(labels_path, "train")
val_labels_path = os.path.join(labels_path, "val")

# # train, val 폴더 생성
# os.makedirs(train_images_path, exist_ok=True)
# os.makedirs(val_images_path, exist_ok=True)
# os.makedirs(train_labels_path, exist_ok=True)
# os.makedirs(val_labels_path, exist_ok=True)

# 이미지와 라벨 데이터 가져오기
images = os.listdir(images_path)
labels = os.listdir(labels_path)

# train, val로 데이터 나누기
train_images, val_images, train_labels, val_labels = train_test_split(
    images, labels, test_size=0.2, random_state=42
)

# train 데이터 복사
for img in train_images:
    img_path = os.path.join(images_path, img)
    label_path = os.path.join(labels_path, img_path[:-4] + ".txt")
    shutil.copy(img_path, os.path.join(train_images_path, img))
    shutil.copy(label_path, os.path.join(train_labels_path, img_path[:-4] + ".txt"))

# val 데이터 복사
for img in val_images:
    img_path = os.path.join(images_path, img)
    label_path = os.path.join(labels_path, img_path[:-4] + ".txt")
    shutil.copy(img_path, os.path.join(val_images_path, img))
    shutil.copy(label_path, os.path.join(val_labels_path, img_path[:-4] + ".txt"))

# for img in images[:2]:
#     img_path = os.path.join(images_path, img)
#     label_path = os.path.join(labels_path, img_path[:-4] + ".txt")
#     print(label_path)