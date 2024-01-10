# import numpy as np
from analytics.rotation_radius import rotation_radius
from analytics.rotation_direction import rotation_direction
from analytics.rotation_correction import rotation_correction
from analytics.rotation_animation import rotation_animation
from analytics.rotation_x import rotation_x
from analytics.rotation_y import rotation_y
# from matplotlib.animation import FuncAnimation
# import matplotlib.pyplot as plt
import pandas as pd
import os

# 処理対象のディレクトリ
directory_path = "./data/"

# ディレクトリ内の全てのCSVファイルに対して処理を行う
for filename in os.listdir(directory_path):

    print(f'処理を実行します: {file_path}')

    output_directory = f'./result/{filename}/'
    os.makedirs(output_directory, exist_ok=True)

    rotation_x(filename)
    rotation_y(filename)
    rotation_radius(filename)
    rotation_direction(filename)
    rotation_correction(filename)
    rotation_animation(filename, 100)