import os
import imageio

result_number = 6
output_directory = f'./result/{result_number}/'

# 保存先のディレクトリが存在するか確認
if not os.path.exists(output_directory):
    print(f"ディレクトリ '{output_directory}' が見つかりません。")
    exit()

# 保存されたGIFファイルのリストを取得
gif_files = [f for f in os.listdir(output_directory) if f.endswith('.gif')]
gif_files.sort()  # ファイル名でソート

# 新しいGIFファイルのパス
output_combined_file = f'{output_directory}{result_number}_combined.gif'

# GIFを逐次的に結合して新しいGIFを作成
total_frames = sum(imageio.get_reader(os.path.join(output_directory, gif_file)).get_length() for gif_file in gif_files)
with imageio.get_writer(output_combined_file, duration=16000 / total_frames) as writer:
    for gif_file in gif_files:
        print('gif結合中')
        gif_path = os.path.join(output_directory, gif_file)
        with imageio.get_reader(gif_path) as reader:
            for frame in reader:
                writer.append_data(frame)

print(f'結合完了: {output_combined_file}')