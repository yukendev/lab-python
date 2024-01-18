import numpy as np

def time(file_path, fps, start_frame=0, end_frame=199693):
    # txtファイルからデータを読み込む
    data = np.loadtxt(file_path, usecols=(2, 6))

    # データの範囲を抽出
    extracted_data = data[start_frame:end_frame + 1, :]
    time = np.arange((start_frame), start_frame + len(extracted_data)) / fps

    return time