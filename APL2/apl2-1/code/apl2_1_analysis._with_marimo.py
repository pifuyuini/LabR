import marimo

__generated_with = "0.11.30"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# 实验APL2-1数据处理""")
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    import numpy as np
    import matplotlib.pyplot as plt
    import ysy_plot_utils as ypu
    import pandas as pd
    import os

    plt.rcParams.update(ypu.ysy_settings())
    return np, os, pd, plt, ypu


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## 1 Superconducting resistance changes with temperature""")
    return


@app.cell
def _(pd):
    data_raise2 = pd.read_csv('data/shangsheng2.xls', encoding='latin1', sep='\t', skiprows=2, usecols=[0, 1], names=['R(V)', 'T(K)'])
    resistance2 = data_raise2['R(V)'].values / (0.01)
    temperature2 = data_raise2['T(K)'].values
    return data_raise2, resistance2, temperature2


@app.cell
def _(pd):
    data_fall1 = pd.read_csv('data/xiajiang.xls', encoding='latin1', sep='\t', skiprows=2, usecols=[0, 1], names=['R(V)', 'T(K)'])
    resistance4 = data_fall1['R(V)'].values / (0.01)
    temperature4 = data_fall1['T(K)'].values
    return data_fall1, resistance4, temperature4


@app.cell
def _(plt, resistance2, resistance4, temperature2, temperature4, ypu):
    points = [(93.21, 0.005287), (94.35, 0.007494), (85.28, 0.004613), (86.57, 0.006820)]
    x_vals, y_vals = zip(*points)  # 拆分成 x 和 y

    #plt.figure(figsize=(8, 6), dpi=150)
    plt.figure()
    plt.plot(temperature2, resistance2, label='Raise Curve', zorder=1)
    plt.plot(temperature4, resistance4, label='Fall Curve', zorder=2)
    plt.scatter(x_vals, y_vals, color=ypu.firefly('fred'), label='Change Point', zorder=3, s=200)
    for x, y in points:
        plt.text(x, y, f'({x}, {y})', fontsize=20, verticalalignment='top', horizontalalignment='left', color=ypu.firefly('fblack'))
    plt.xlabel('T [K]')
    plt.ylabel('R [$\Omega$]')
    plt.legend()
    #mo.mpl.interactive(plt.gcf())
    plt.show()
    return points, x, x_vals, y, y_vals


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## 2 Superconducting resistance changes with temperature after applying magnetic field

        Due to the experimental operator's idiotic data naming method, data import can only be carried out in the following abstract way.

        The stupid points include: two paragraphs of characters are connected by a space (this is really stupid, those who can resist criticizing are really smart).

        What's even more stupid is that some of them have blank connections and some don't, and you have to click on them one by one using the rename function. Is this the way a human can name things???
        """
    )
    return


@app.cell
def _(os, pd):
    # 文件夹路径
    folder = 'data'

    # 存储结果的字典
    rise_data = {}  # 上升数据，键是电流（int），值是DataFrame
    fall_data = {}  # 下降数据，键是电流（int），值是DataFrame

    # 遍历0A到8A
    for current_1 in range(1, 9):
        # 构造文件名
        rise_filename = f"{current_1}A上升.xls"
        fall_filename = f"{current_1}A下降.xls"

        # 构造完整路径
        rise_path = os.path.join(folder, rise_filename)
        fall_path = os.path.join(folder, fall_filename)

        # 读取文件
        rise_df = pd.read_csv(rise_path, encoding='latin1', sep='\t', skiprows=2, usecols=[0, 1], names=['R(V)', 'T(K)'])
        fall_df = pd.read_csv(fall_path, encoding='latin1', sep='\t', skiprows=2, usecols=[0, 1], names=['R(V)', 'T(K)'])

        # 存入字典
        rise_data[current_1] = rise_df
        fall_data[current_1] = fall_df
    return (
        current_1,
        fall_data,
        fall_df,
        fall_filename,
        fall_path,
        folder,
        rise_data,
        rise_df,
        rise_filename,
        rise_path,
    )


@app.cell
def _(plt, rise_data, ypu):
    ypu.liuyin_color_theme()

    # 画 rise 数据图
    plt.figure()
    for current_2, df_2 in rise_data.items():
        plt.plot(df_2['T(K)'], df_2['R(V)'].values/0.01, label=f'{current_2}A')
    plt.xlabel('T [K]')
    plt.ylabel('R [$\Omega$]')
    plt.title('Rise Data')
    plt.legend(title='Current')
    plt.tight_layout()
    plt.show()

    return current_2, df_2


@app.cell
def _(fall_data, plt):
    # 画 fall 数据图
    plt.figure()
    for current_3, df_3 in fall_data.items():
        plt.plot(df_3['T(K)'], df_3['R(V)'].values/0.01, label=f'{current_3}A')
    plt.xlabel('T [K]')
    plt.ylabel('R [$\Omega$]')
    plt.title('Fall Data')
    plt.legend(title='Current')
    plt.tight_layout()
    plt.show()
    return current_3, df_3


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""由于这个笔记本不太方便和GPT配合，后续处理转到jupyter上……""")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
