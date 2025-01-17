import os
import shutil

def select_file():
    # 使用Kivy的FileChooser实现文件选择，略
    pass
AZ
def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def zip_file(file_path, output_zip):
    shutil.make_archive(output_zip, 'zip', os.path.dirname(file_path), os.path.basename(file_path))
