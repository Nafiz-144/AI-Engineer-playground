
import os

directory_path = '.'  # current folder

try:
    contents = os.listdir(directory_path)
    for item in contents:
        print(item)
except Exception as e:
    print("Error:", e)