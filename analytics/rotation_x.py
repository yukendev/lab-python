import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def rotation_x(cell_number, file_path, output_directory, fps, start_frame=0, end_frame=199693):
    
    # txtファイルからデータを読み込む
    data = np.loadtxt(file_path, usecols=(2, 6))

    # データの範囲を抽出
    extracted_data = data[start_frame:end_frame + 1, :]

    # 時間の計算
    time = np.arange(start_frame, start_frame + len(extracted_data)) / fps

    # グラフの描画
    plt.figure(figsize=(30, 5))
    plt.plot(time, extracted_data[:, 0])
    plt.title(str(cell_number) + ": x")
    plt.xlabel('Time (seconds)')
    plt.ylabel('x')
    plt.grid(True)
    # plt.show()

    plt.savefig(output_directory + cell_number + "_rotation_x.png")
