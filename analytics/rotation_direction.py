import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def get_rotation_direction(from_point, to_point, reference_point):
    # 始点または終点が基準点と同じ場合、回転方向は定義しない
    if from_point == reference_point or to_point == reference_point:
        print('エラー')
        return 'undefined'

    # 始点と終点からベクトルを計算
    reference_point = np.array(reference_point)
    from_vector = np.array(from_point) - reference_point
    to_vector = np.array(to_point) - reference_point

    # 外積を計算
    cross_product = np.cross(from_vector, to_vector)

    return np.sign(cross_product)


def rotation_direction(cell_number, file_path, output_directory, fps, start_frame=0, end_frame=199693):

    # txtファイルからデータを読み込む
    data = np.loadtxt(file_path, usecols=(2, 6))

    # データの範囲を抽出
    extracted_data = data[start_frame:end_frame + 1, :]

    # 重心座標の計算
    center_x = np.mean(extracted_data[:, 0])
    center_y = np.mean(extracted_data[:, 1])

    rotation_angles = []

    buffer = 100

    for i in range(len(extracted_data[:, 0]) - (buffer + 1)):
        x_n, y_n = extracted_data[:, 0][i], extracted_data[:, 1][i]
        x_n1, y_n1 = extracted_data[:, 0][i + (buffer + 1)], extracted_data[:, 1][i + (buffer + 1)]

        # n番目の点からn+1番目の点が重心に対してどれだけ回転したかを計算
        rotation_angle = get_rotation_direction((x_n, y_n), (x_n1, y_n1), (center_x, center_y))

        rotation_angles.append(rotation_angle)

    # 時間の計算
    time = np.arange(start_frame, start_frame + len(extracted_data)) / fps

    # グラフの描画
    plt.figure(figsize=(30, 5))
    plt.plot(time[:-(buffer + 1)], rotation_angles, c="red")
    # plt.scatter(time[:-(buffer + 1)], rotation_angles, label='Rotation Radius', s = 0.1, c="red")
    plt.title(str(cell_number) + ': Rotation Radius')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Rotation Radius')
    # plt.legend()
    plt.grid(True)
    # plt.show()

    plt.savefig(output_directory + cell_number + "_rotation_direction.png")