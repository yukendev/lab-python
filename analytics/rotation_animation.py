import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation

def rotation_animation(file_name, data):
    # 重心座標の計算
    center_x = np.mean(data[:, 0])
    center_y = np.mean(data[:, 1])

    # グラフの設定
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.grid(True)

    print('計算開始')

    # ArtistAnimationの初期化
    frames = []
    sc = ax.scatter([], [], marker='o', color='red', s=50, label='Center of Mass')
    ax.legend()

    for frame in range(len(data)):
        print('計算中...'+ str(frame) + '/' + str(len(data)))
        if frame > 0:
            center = [np.mean(data[:frame, 0]), np.mean(data[:frame, 1])]
            sc.set_offsets([center])  # プロットの更新
        else:
            center = [0, 0]  # 最初のフレームの場合、中心を[0, 0]と仮定する
        frames.append([sc])


    print('計算終了')

    # ArtistAnimationの作成
    animation = ArtistAnimation(fig, frames)

    # アニメーションを表示
    plt.show()

    print('保存開始')
    # 動画の保存
    animation.save('center_of_mass_animation_artist.gif')
    # animation.save('center_of_mass_animation.mp4', writer='ffmpeg', fps=30)
    # animation.save('center_of_mass_animation.gif', writer='imagemagick', fps=30)
    # animation.save('center_of_mass_animation.mp4')
    print('保存終了')
    # 表示
    # アニメーションの保存が完了するまで待つ
    plt.close(fig)
