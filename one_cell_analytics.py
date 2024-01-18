# from analytics.rotation_radius import rotation_radius
from analytics.rotation_direction import rotation_direction
from analytics.rotation_correction import rotation_correction
from analytics.rotation_animation import rotation_animation
from analytics.rotation_x import rotation_x
from analytics.rotation_y import rotation_y
from analytics.rotation_fit_circle import rotation_fit_circle
import os

# 解析対象のcell番号
cell_number="1220_2_7"

fps=12500.0

# {start_second}秒から{end_second}秒までを解析
start_second=0.365
end_second=0.383

# {start_frame}フレームから{end_frame}フレームまでを解析
start_frame = start_second * fps
end_frame = end_second * fps

# 解析対象の重心位置データファイル
file_path = f'./data/cell_{cell_number}.txt'

# 結果出力ディレクトリ
output_directory = f'./result/one_cell_analytics/{cell_number}/'
os.makedirs(output_directory, exist_ok=True)

print(f'処理を実行します: {file_path}')

# n個の点を円と近似した場合の横軸時間で『回転速度(rad/sec)』と『回転半径』をグラフ出力する関数
rotation_fit_circle(cell_number, file_path, output_directory, fps, int(start_frame), int(end_frame))

# 横軸『時間(sec)』縦軸『x座標』をグラフ出力する関数
rotation_x(cell_number, file_path, output_directory, fps, int(start_frame), int(end_frame))

# 横軸『時間(sec)』縦軸『y座標』をグラフ出力する関数
rotation_y(cell_number, file_path, output_directory, fps, int(start_frame), int(end_frame))

# 横軸『時間(sec)』縦軸『回転方向』をグラフ出力する関数
rotation_direction(cell_number, file_path, output_directory, fps, int(start_frame), int(end_frame))

rotation_correction(cell_number, file_path, output_directory, fps, int(start_frame), int(end_frame))

# 重心の回転の様子をアニメーション出力する関数
# rotation_animation(cell_number, file_path, output_directory, fps)