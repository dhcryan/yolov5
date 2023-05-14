import os

dir_path = r'C:\Users\dhc40\vision\23_ML\yolov5\data3\labels\train'
class_counts = {'0': 0, '1': 0}

for file_name in os.listdir(dir_path):
    file_path = os.path.join(dir_path, file_name)
    with open(file_path, 'r') as f:
        for line in f:
            class_id, _, _, _, _ = line.strip().split()
            class_counts[class_id] += 1

print(f'클래스 0의 개수: {class_counts["0"]}')
print(f'클래스 1의 개수: {class_counts["1"]}')
