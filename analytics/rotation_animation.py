import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd
import os
import cv2
import numpy as np

# 動画を読み込み、FPSを変更して別名で保存する関数
def m_speed_change(path_in, path_out, scale_factor, color_flag):
    # 動画読み込みの設定
    movie = cv2.VideoCapture(path_in)
 
    # 動画ファイル保存用の設定
    fps = int(movie.get(cv2.CAP_PROP_FPS))                                  # 元動画のFPSを取得
    fps_new = int(fps * scale_factor)                                       # 動画保存時のFPSはスケールファクターをかける
    w = int(movie.get(cv2.CAP_PROP_FRAME_WIDTH))                            # 動画の横幅を取得
    h = int(movie.get(cv2.CAP_PROP_FRAME_HEIGHT))                           # 動画の縦幅を取得
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')                     # 動画保存時のfourcc設定（mp4用）
    video = cv2.VideoWriter(path_out, fourcc, fps_new, (w, h), color_flag)  # 動画の仕様（ファイル名、fourcc, FPS, サイズ）
 
    # ファイルからフレームを1枚ずつ取得して動画処理後に保存する
    while True:
        ret, frame = movie.read()        # フレームを取得
        video.write(frame)               # 動画を保存する
        # フレームが取得できない場合はループを抜ける
        if not ret:
            break
    # 撮影用オブジェクトとウィンドウの解放
    movie.release()
    return





def rotation_animation(cell_number, file_path, output_directory, fps):

    num_points=100 # アニメーションの各フレームで表示するデータの終了インデックス

     # txtファイルからデータを読み込む
    data = np.loadtxt(file_path, usecols=(2, 6))

    # グローバルスコープで line を定義
    line = []

    # 更新する内容
    def _update_plot(i, fig, line):
        start_index = i  # アニメーションの各フレームで表示するデータの開始インデックス
        end_index = start_index + num_points  # アニメーションの各フレームで表示するデータの終了インデックス
        # データのスライス
        x_data = data[start_index:end_index, 0]
        y_data = data[start_index:end_index, 1]
        print('処理中...', i)

        # 前回のフレーム内容を一旦削除
        if len(line) > 0:
            line[0].remove()
        if len(sc) > 0:
            sc[0].remove()

        # 現在のフレームの点をプロット
        line.clear()  # 現在のフレームの線を保持するリストをクリア
        line.append(plt.plot(x_data, y_data, color='blue')[0])

        # 現在のフレームの点をプロット
        sc.clear()  # 現在のフレームの点を保持するリストをクリア
        sc.append(plt.scatter(x_data, y_data, color='red'))

    fig =  plt.figure()

    # グラフを中央に表示
    ax = fig.add_subplot(1,1,1)


    # # データの最小値と最大値を取得
    min_x, max_x = data[:, 0].min(), data[:, 0].max()
    min_y, max_y = data[:, 1].min(), data[:, 1].max()

    # グラフの目盛範囲設定
    ax.set_xlim([min_x, max_x])
    ax.set_ylim([min_y, max_y])

    line = []  # フレーム更新の際に前回のプロットを削除するために用意
    sc = []    # フレーム更新の際に前回の点を削除するために用意

    # アニメーション作成
    interval = 1 / fps * 1000  # ミリ秒単位に変換
    ani = animation.FuncAnimation(fig, _update_plot, fargs = (fig, line), 
        frames = len(data) - 9, interval = interval, repeat = False)


    # plt.show()

    # アニメーションを保存
    print('保存開始')
    output_file = f'{output_directory}{cell_number}_animation.mp4'
    ani.save(output_file)
    print(f'保存完了: {output_file}')

    print('動画を10倍速にします')
    processed_video_output_file = f'{output_directory}{cell_number}_animation_processed.mp4'
    path_in = output_file       # 元動画のパス
    path_out = processed_video_output_file      # 保存する動画のパス
    scale_factor = 10              # FPSにかけるスケールファクター
    color_flag = True               # カラー動画はTrue, グレースケール動画はFalse
    
    # 動画の再生速度を変更する関数を実行
    m_speed_change(path_in, path_out, scale_factor, color_flag)


