import numpy as np
from analytics.rotation_radius import rotation_radius
from analytics.rotation_direction import rotation_direction
from analytics.rotation_correction import rotation_correction
from analytics.rotation_animation import rotation_animation

result_number = 6

# ファイルのパス
file_path = "./data/result_" + str(result_number) + ".csv"


# BOMを削除してからデータを読み込む
with open(file_path, 'r', encoding='utf-8-sig') as file:
    data = np.loadtxt(file, delimiter=',')

rotation_radius(str(result_number), data)
rotation_direction(str(result_number), data)
rotation_correction(str(result_number), data)
rotation_animation(str(result_number), data)