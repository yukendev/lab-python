import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def rotation_correction(cell_number, file_path, output_directory, fps):

    # txtファイルからデータを読み込む
    data = np.loadtxt(file_path, usecols=(2, 6))
    
    # 重心座標の計算
    center_x = np.mean(data[:, 0])
    center_y = np.mean(data[:, 1])

    # 回転角の計算
    theta = np.arctan2(data[:, 1] - center_y, data[:, 0] - center_x)


    # 回転の補正
    rotated_x = center_x + (data[:, 0] - center_x) * np.cos(theta) - (data[:, 1] - center_y) * np.sin(theta)
    rotated_y = center_y + (data[:, 0] - center_x) * np.sin(theta) + (data[:, 1] - center_y) * np.cos(theta)

    # グラフの描画（元の姿勢と補正後の姿勢）
    plt.figure(figsize=(10, 5))

    # 元の姿勢
    plt.subplot(1, 2, 1)
    plt.scatter(data[:, 0], data[:, 1], label='Original Position')
    # plt.scatter(data[0, 0], data[0, 1], color='r', marker='o', label='Initial Position (Red Dot)')
    plt.title('Original Position')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()

    # グラフの目盛範囲設定
    # plt.xlim([-100, 100])
    # plt.ylim([-100, 100])


    # 補正後の姿勢
    plt.subplot(1, 2, 2)
    plt.scatter(rotated_x, rotated_y, label='Rotated Position')
    plt.scatter(rotated_x[0], rotated_y[0], color='r', marker='o', label='Initial Position (Red Dot)')
    plt.title('Rotated Position')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()

    # グラフの目盛範囲設定
    # plt.xlim([-100, 100])
    # plt.ylim([-100, 100])

    # plt.show()

    plt.savefig(output_directory + cell_number + "_rotation_correction.png")

  