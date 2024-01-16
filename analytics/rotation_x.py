import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def rotation_x(cell_number, file_path, output_directory):
    
    # txtファイルからデータを読み込む
    data = np.loadtxt(file_path, usecols=(2, 6))

    # 時間の計算（1秒あたりのフレーム数は12500fps）
    time = np.arange(0, len(data)) / 12500.0

    # グラフの描画
    plt.figure(figsize=(20, 5))
    plt.plot(time, data[:, 0], label='x座標')
    plt.title("x: " + str(cell_number))
    plt.xlabel('Time (seconds)')
    plt.ylabel('x座標')
    plt.legend()
    plt.grid(True)
    # plt.show()

    plt.savefig(output_directory + cell_number + "_rotation_x.png")