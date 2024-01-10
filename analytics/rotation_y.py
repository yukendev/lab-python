import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def rotation_y(file_name):
    file_path = "./data/" + str(file_name)

    # txtファイルからデータを読み込む
    data = np.loadtxt(file_path, usecols=(2, 6))

    # 時間の計算（1秒あたりのフレーム数は12500fps）
    time = np.arange(0, len(data)) / 12500.0

    # グラフの描画
    plt.figure(figsize=(20, 5))
    plt.plot(time, data[:, 1], label='y座標')
    plt.title("y: " + str(file_name))
    plt.xlabel('Time (seconds)')
    plt.ylabel('y座標')
    plt.legend()
    plt.grid(True)
    # plt.show()

    output_directory = f'./result/{file_name}/'

    plt.savefig(output_directory + file_name + "_rotation_y.png")