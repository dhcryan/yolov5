import os

img_path = r'C:\Users\dhc40\vision\23_ML\yolov5\data5\images'
img_list = os.listdir(img_path)
img_list.sort()
for i, name in enumerate(img_list):
    src = os.path.join(img_path, name)
    dst = os.path.join(img_path, str(i+4735) + '.jpg')
    os.rename(src, dst)
