import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd

result_number = 2
file_path = "./data/result_" + str(result_number) + ".csv"
data = pd.read_csv(file_path, header=None, names=['x', 'y'])

# 更新する内容
def _update_plot(i, fig, im):
    x_data = data.iloc[i]['x']  # CSVファイルの'x'列
    y_data = data.iloc[i]['y']  # CSVファイルの'y'列
    print('処理中...', i)

    # 前回のフレーム内容を一旦削除
    if len(im) > 0:
        im[0].remove()
        im.pop()

    im.append(plt.scatter(x_data, y_data, color='red'))

fig =  plt.figure()

# グラフを中央に表示
ax = fig.add_subplot(1,1,1)

# データの最小値と最大値を取得
min_x, max_x = data['x'].min(), data['x'].max()
min_y, max_y = data['y'].min(), data['y'].max()

# グラフの目盛範囲設定
ax.set_xlim([min_x, max_x])
ax.set_ylim([min_y, max_y])

im = [] # フレーム更新の際に前回のプロットを削除するために用意

# アニメーション作成
fps = 12500
interval = 1 / fps * 1000  # ミリ秒単位に変換
print('intervalは', interval)
ani = animation.FuncAnimation(fig, _update_plot, fargs = (fig, im), 
        frames = len(data), interval = 1, repeat = False)

# 199692
print('保存開始')
ani.save('hogehoge.mp4')
print('保存終了')