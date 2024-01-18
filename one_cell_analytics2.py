from analytics2.rotation_direction import rotation_direction
from analytics2.rotation_x import rotation_x
from analytics2.rotation_y import rotation_y
from analytics2.rotation_fit_circle import rotation_fit_circle
from analytics2.time import time
import os
import matplotlib.pyplot as plt
import numpy as np

# 解析対象のcell番号
cell_number="1220_2_7"

fps=12500.0

# {start_second}秒から{end_second}秒までを解析
start_second=0
end_second=0.1

# {start_frame}フレームから{end_frame}フレームまでを解析
start_frame = start_second * fps
end_frame = end_second * fps

# 解析対象の重心位置データファイル
file_path = f'./data/cell_{cell_number}.txt'

# 結果出力ディレクトリ
output_directory = f'./result/one_cell_analytics/{cell_number}/'
os.makedirs(output_directory, exist_ok=True)

print(f'処理を実行します: {file_path}')

# サブプロットの設定
fig, axes = plt.subplots(nrows=5, ncols=1, figsize=(30, 5))

# 時間の計算
time_data = time(file_path, fps, int(start_frame), int(end_frame))


# 横軸『時間(sec)』縦軸『x座標』
x_data = rotation_x(file_path, fps, int(start_frame), int(end_frame))
axes[0].plot(time_data, x_data)
axes[0].set_title(str(cell_number) + ": x")
# axes[0].set_xlabel('Time (seconds)')
axes[0].set_ylabel('x')
axes[0].grid(True)


# 横軸『時間(sec)』縦軸『y座標』
y_data = rotation_y(file_path, fps, int(start_frame), int(end_frame))
axes[1].plot(time_data, y_data, color='red')
axes[1].set_title(str(cell_number) + ": y")
# axes[1].set_xlabel('Time (seconds)')
axes[1].set_ylabel('y')
axes[1].grid(True)


# 横軸『時間(sec)』縦軸『回転方向』
direction_data = rotation_direction(file_path, fps, int(start_frame), int(end_frame))
# 時間データと配列の長さを揃えるため、足りない部分は0で埋め尽くす
direction_data_padded = np.pad(direction_data, (0, len(time_data) - len(direction_data)), constant_values=0)
axes[2].plot(time_data, direction_data_padded, color='green')
axes[2].set_title(str(cell_number) + ": rotation direction")
# axes[2].set_xlabel('Time (seconds)')
axes[2].set_ylabel('direction')
axes[2].grid(True)


# n個の点を円と近似した場合の横軸時間で『回転速度(rad/sec)』と『回転半径』
angle_velocity_data, radius_data = rotation_fit_circle(file_path, fps, int(start_frame), int(end_frame))
# 時間データと配列の長さを揃えるため、足りない部分は0で埋め尽くす
angle_velocity_data_padded = np.pad(angle_velocity_data, (0, len(time_data) - len(angle_velocity_data)), constant_values=0)
axes[3].plot(time_data, angle_velocity_data_padded, color='purple')
axes[3].set_title(str(cell_number) + ": rotation angle velocity")
# axes[3].set_xlabel('Time (seconds)')
axes[3].set_ylabel('angle velocity(rad/sec)')
axes[3].grid(True)


radius_data_padded = np.pad(radius_data, (0, len(time_data) - len(radius_data)), constant_values=0)
axes[4].plot(time_data, angle_velocity_data_padded, color='yellow')
axes[4].set_title(str(cell_number) + ": rotation angle radius")
# axes[4].set_xlabel('Time (seconds)')
axes[4].set_ylabel('radius')
axes[4].grid(True)


# グラフの間隔を調整
plt.tight_layout()

# 全体のタイトル
# plt.suptitle('Multiple Plots')

# 画像の保存や表示
plt.savefig(output_directory + cell_number + "analytics2.png")
plt.show()