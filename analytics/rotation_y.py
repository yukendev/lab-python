import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def rotation_y(cell_number, file_path, output_directory, fps):

    # txtファイルからデータを読み込む
    data = np.loadtxt(file_path, usecols=(2, 6))

    # 時間の計算
    time = np.arange(0, len(data)) / fps

    # グラフの描画
    plt.figure(figsize=(20, 5))
    plt.plot(time, data[:, 1], label='y座標')
    plt.title("y: " + str(cell_number))
    plt.xlabel('Time (seconds)')
    plt.ylabel('y座標')
    plt.legend()
    plt.grid(True)
    # plt.show()

    plt.savefig(output_directory + cell_number + "_rotation_y.png")