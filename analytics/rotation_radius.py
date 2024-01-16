import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def rotation_radius(cell_number, file_path, output_directory):

    # txtファイルからデータを読み込む
    data = np.loadtxt(file_path, usecols=(2, 6))

    # # 重心座標の計算
    center_x = np.mean(data[:, 0])
    center_y = np.mean(data[:, 1])

    # 回転角の計算
    theta = np.arctan2(data[:, 1] - center_y, data[:, 0] - center_x)

    # 回転の補正
    rotated_x = center_x + (data[:, 0] - center_x) * np.cos(theta) - (data[:, 1] - center_y) * np.sin(theta)
    rotated_y = center_y + (data[:, 0] - center_x) * np.sin(theta) + (data[:, 1] - center_y) * np.cos(theta)

    # 回転半径の計算
    rotation_radius = np.sqrt((rotated_x - center_x)**2 + (rotated_y - center_y)**2)

    # 回転方向に応じて符号を反転
    rotation_radius *= np.sign(theta)

    # 時間の計算（1秒あたりのフレーム数は12500fps）
    time = np.arange(0, len(data)) / 12500.0

    # グラフの描画
    plt.figure(figsize=(20, 5))
    plt.plot(time, rotation_radius, label='Rotation Radius')
    plt.title('Rotation Radius over Time')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Rotation Radius')
    plt.legend()
    plt.xlim(0, 4)
    plt.grid(True)
    # plt.show()

    plt.savefig(output_directory + cell_number + "_rotation_radius.png")