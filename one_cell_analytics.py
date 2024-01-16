from analytics.rotation_radius import rotation_radius
from analytics.rotation_direction import rotation_direction
from analytics.rotation_correction import rotation_correction
from analytics.rotation_animation import rotation_animation
from analytics.rotation_x import rotation_x
from analytics.rotation_y import rotation_y
import os

# 解析対象のcell番号
cell_number="1220_1_1"

# {start_second}秒から{end_second}秒までを解析
start_second=0
end_second=16

fps=12500.0

# 解析対象の重心位置データファイル
file_path = f'./data/cell_{cell_number}.txt'

# 結果出力ディレクトリ
output_directory = f'./result/one_cell_analytics/{cell_number}/'
os.makedirs(output_directory, exist_ok=True)

print(f'処理を実行します: {file_path}')

rotation_x(cell_number, file_path, output_directory, fps)
rotation_y(cell_number, file_path, output_directory, fps)
rotation_radius(cell_number, file_path, output_directory, fps)
rotation_direction(cell_number, file_path, output_directory, fps)
rotation_correction(cell_number, file_path, output_directory, fps)
rotation_animation(cell_number, file_path, output_directory, fps)