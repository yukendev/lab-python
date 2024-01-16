from analytics.rotation_radius import rotation_radius
from analytics.rotation_direction import rotation_direction
from analytics.rotation_correction import rotation_correction
from analytics.rotation_animation import rotation_animation
from analytics.rotation_x import rotation_x
from analytics.rotation_y import rotation_y
import os
import re

# 処理対象のディレクトリ
directory_path = "./data/"

fps=12500.0

# ディレクトリ内の全てのCSVファイルに対して処理を行う
for filename in os.listdir(directory_path):

    pattern = r'cell_(\d+_\d+_\d+)\.txt'
    match = re.search(pattern, filename)

    if match:
        cell_number = match.group(1)
        output_directory = f'./result/{cell_number}/'
        os.makedirs(output_directory, exist_ok=True)

        file_path = f'./data/cell_{cell_number}.txt'

        print(f'処理を実行します: {file_path}')

        rotation_x(cell_number, file_path, output_directory)
        rotation_y(cell_number, file_path, output_directory)
        rotation_radius(cell_number, file_path, output_directory)
        rotation_direction(cell_number, file_path, output_directory)
        rotation_correction(cell_number, file_path, output_directory)
        rotation_animation(cell_number, file_path, output_directory, fps)
    else:
        print("ファイル名が正しくありません", file_path)