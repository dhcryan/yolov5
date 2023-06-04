import os
import shutil

img_path = r'C:\Users\dhc40\Downloads\drive-download-20230522T041113Z-001\3rd_1_done\1\image'
txt_path = r'C:\Users\dhc40\Downloads\drive-download-20230522T041113Z-001\3rd_1_done\1\label'
img_new_path = r'C:\Users\dhc40\Downloads\drive-download-20230522T041113Z-001\3rd_1_done\1\new_image'
txt_new_path = r'C:\Users\dhc40\Downloads\drive-download-20230522T041113Z-001\3rd_1_done\1\new_label'
# Get the list of files in img and txt directories
img_files = os.listdir(img_path)
txt_files = os.listdir(txt_path)

# Remove file extensions from file names
img_files_no_ext = [os.path.splitext(file)[0] for file in img_files]
txt_files_no_ext = [os.path.splitext(file)[0] for file in txt_files]

# Find common file names between img and txt directories
common_files = set(img_files_no_ext) & set(txt_files_no_ext)

# Move image files with common names from img_path to img_new_path
for file in common_files:
    image_file = file + '.jpg'
    text_file = file + '.txt'
    if image_file in img_files:
        shutil.move(os.path.join(img_path, image_file), os.path.join(img_new_path, image_file))
    if text_file in txt_files:
        shutil.move(os.path.join(txt_path, text_file), os.path.join(txt_new_path, text_file))