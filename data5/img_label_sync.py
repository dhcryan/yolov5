import os
import shutil

image_folder = r"C:\Users\dhc40\vision\23_ML\yolov5\data5\images"
label_folder = r"C:\Users\dhc40\vision\23_ML\yolov5\data5\labels"
destination_folder = r"C:\Users\dhc40\vision\23_ML\yolov5\data5\val"

# 이미지 폴더의 파일 목록 가져오기
image_files = os.listdir(image_folder)

for image_file in image_files:
    # 이미지 파일의 이름과 확장자 분리
    file_name, file_extension = os.path.splitext(image_file)
    
    # 이미지 파일에 해당하는 txt 파일 경로 생성
    label_file = os.path.join(label_folder, file_name + ".txt")
    
    # txt 파일이 존재하는지 확인하고, 있다면 다른 폴더로 이동
    if os.path.isfile(label_file):
        shutil.move(label_file, destination_folder)
