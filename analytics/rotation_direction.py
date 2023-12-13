import numpy as np
import matplotlib.pyplot as plt

def rotation_direction(file_name, data):
    # 重心座標の計算
    center_x = np.mean(data[:, 0])
    center_y = np.mean(data[:, 1])

    # 回転角の計算
    theta = np.arctan2(data[:, 1] - center_y, data[:, 0] - center_x)

    # 時間の計算（1秒あたりのフレーム数は12500fps）
    time = np.arange(0, len(data)) / 12500.0

    # グラフの描画
    plt.figure(figsize=(10, 5))
    plt.plot(time, np.sign(theta), label='Rotation Radius')
    plt.title('Rotation Radius over Time')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Rotation Radius')
    plt.legend()
    plt.xlim(0, 1)
    plt.grid(True)
    plt.show()
    plt.savefig("./result/" + file_name + "_rotation_direction.png")