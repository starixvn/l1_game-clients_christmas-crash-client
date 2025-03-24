#!/usr/bin/python

import os
import shutil
import subprocess

if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.realpath(__file__))
    project_dir = os.path.join(current_dir, '')

    # Danh sách các thư mục cần xử lý
    image_dirs = [
        "./images/atlas-en",
        "./images/atlas-id",
        "./images/atlas-vi",
        "./images/atlas-zh_cn",
        "./images/atlas-zh_tw",
        "./images/atlas-th",
    ]

    # Pack.
    packer_path = os.path.join(
        project_dir,
        'pack.js'
    )

    outputPath = os.path.join(project_dir, '..\\', 'src\\assets\\resources\\i18n-atlas')

    # Xử lý từng thư mục
    for images_dir in image_dirs:
        print(f"Đang xử lý thư mục: {images_dir}")
        subprocess.Popen([
            'node',
            packer_path,
            '-t',
            'remote',
            '-a',
            'http://10.10.50.17:3456',
            '-i',
            os.path.join(project_dir, images_dir, 'texture_packer.json'),
            '-o',
            outputPath
        ]).wait()

