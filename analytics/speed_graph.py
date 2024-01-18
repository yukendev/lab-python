import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def speed_graph(cell_number, output_directory, time, rotation_angle_velocity_array, fit_points):

    # 回転半径グラフの描画
    plt.figure(figsize=(20, 5))
    plt.plot(time[:-(fit_points - 1)], rotation_angle_velocity_array, label='Rotational speed')
    plt.title(str(cell_number) + f': {fit_points} points fit circle rotational speed')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Rotational speed(rad/second)')
    plt.axhline(0, color='red', linestyle='--', linewidth=2)
    plt.legend()
    plt.grid(True)

    plt.savefig(output_directory + cell_number + "_rotation_fit_circle_speed.png")