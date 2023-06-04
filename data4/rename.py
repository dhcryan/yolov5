import os

img_path = r'C:\Users\dhc40\vision\23_ML\yolov5\data4\3rd_3_done\3_done\labels'
img_list = os.listdir(img_path)
img_list.sort()
for i, name in enumerate(img_list):
    src = os.path.join(img_path, name)
    dst = os.path.join(img_path, str(i+3258) + '.txt')
    os.rename(src, dst)
