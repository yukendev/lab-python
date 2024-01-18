import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from analytics.radius_graph import radius_graph
from analytics.speed_graph import speed_graph

# 100個の点で円と近似
fit_points = 500

def get_angle(point_a, point_b, reference_point, is_radian=False):
    # 点Aまたは点Bが基準点と同じ場合、角度は0を返す
    if point_a == reference_point or point_b == reference_point:
        return 0

    # ベクトルを計算
    reference_point = np.array(reference_point)
    vector_a = np.array(point_a) - reference_point
    vector_b = np.array(point_b) - reference_point

    # ベクトルの大きさ(長さ)を計算
    magnitude_a = np.linalg.norm(vector_a)
    magnitude_b = np.linalg.norm(vector_b)

    # 内積を計算
    dot_product = np.dot(vector_a, vector_b)

    # 余弦を計算
    cosine = dot_product / (magnitude_a * magnitude_b)

    # 逆余弦関数を計算して角度を取得
    angle = np.arccos(cosine)

    # 弧度法指定ではない場合、角度を度数法に変換
    return angle if is_radian else np.degrees(angle)


def get_rotation_direction(from_point, to_point, reference_point):
    # 始点または終点が基準点と同じ場合、回転方向は定義しない
    if from_point == reference_point or to_point == reference_point:
        return 'undefined'

    # 始点と終点からベクトルを計算
    reference_point = np.array(reference_point)
    from_vector = np.array(from_point) - reference_point
    to_vector = np.array(to_point) - reference_point

    # 外積を計算
    cross_product = np.cross(from_vector, to_vector)

    # 外積の符号に応じて角度を調整
    return 'anti-clockwise' if cross_product >= 0 else 'clockwise'

def get_signed_angle(from_point, to_point, reference_point, is_radian=False):
    angle = get_angle(from_point, to_point, reference_point, is_radian)
    rotation_direction = get_rotation_direction(from_point, to_point, reference_point)

    return angle if rotation_direction == 'anti-clockwise' else -angle


def selected_points_analytics(selected_points, fps):

    # 抽出された点の中心座標
    selected_points_x_center = np.mean(selected_points[:, 0])
    selected_points_y_center = np.mean(selected_points[:, 1])

    # 回転角の計算
    theta = np.arctan2(selected_points[:, 1] - selected_points_y_center, selected_points[:, 0] - selected_points_x_center)

    # 回転の補正
    rotated_x = selected_points_x_center + (selected_points[:, 0] - selected_points_x_center) * np.cos(theta) - (selected_points[:, 1] - selected_points_y_center) * np.sin(theta)
    rotated_y = selected_points_y_center + (selected_points[:, 0] - selected_points_x_center) * np.sin(theta) + (selected_points[:, 1] - selected_points_y_center) * np.cos(theta)

    rotation_angle_velocity_array = []
    # 回転速度の計算
    for i in range(len(selected_points[:, 0])):
        # {fit_points}個の点を円と近似すると、{fit_points-1}個の角度が出てくる
        if i == fit_points - 1:
            break
        # x_n, y_n = selected_points[:, 0][i], selected_points[:, 1][i]
        # x_n1, y_n1 = selected_points[:, 0][i + 1], selected_points[:, 1][i + 1]
        x_n, y_n = rotated_x[i], rotated_y[i]
        x_n1, y_n1 = rotated_x[i + 1], rotated_y[i + 1]


        rotation_angle_velocity = get_signed_angle((x_n, y_n), (x_n1, y_n1), (selected_points_x_center, selected_points_y_center), True) / (1 / fps)

        rotation_angle_velocity_array.append(rotation_angle_velocity)

    rotation_radius_array = np.sqrt((rotated_x - selected_points_x_center)**2 + (rotated_y - selected_points_y_center)**2)

    return np.mean(rotation_angle_velocity_array), np.mean(rotation_radius_array)



def rotation_fit_circle(cell_number, file_path, output_directory, fps, start_frame=0, end_frame=199693):
    
    # txtファイルからデータを読み込む
    data = np.loadtxt(file_path, usecols=(2, 6))

    # データの範囲を抽出
    extracted_data = data[start_frame:end_frame + 1, :]

    rotation_angle_velocity_array = []
    rotation_radius_array = []
    for i in range(len(extracted_data[:, 0])):

        print('処理中...', i)

        selected_points = extracted_data[i : i + fit_points]

        # fit_points個の点を抽出できなくなった時点で終了
        if len(selected_points) < fit_points:
            break

        rotation_angle_velocity, rotation_radius = selected_points_analytics(selected_points, fps)

        rotation_angle_velocity_array.append(rotation_angle_velocity)
        rotation_radius_array.append(rotation_radius)


    # 時間の計算
    time = np.arange(start_frame, start_frame + len(extracted_data)) / fps

    # 回転速度グラフの描画
    speed_graph(cell_number, output_directory, time, rotation_angle_velocity_array, fit_points)

    # 回転半径グラフの描画
    radius_graph(cell_number, output_directory, time, rotation_radius_array, fit_points)
