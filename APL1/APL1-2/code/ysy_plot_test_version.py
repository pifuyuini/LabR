# 尝试编写个人标准绘图库
# ysy_plot.py
# copyright@pifuyuini
# version: 1.0.0
# update: 20250104

# Import necessary package
import matplotlib.pyplot as plt

# Settings
def ysy_settings():
    '''
    
    '''
    # Style
    plt.style.use('seaborn-v0_8-whitegrid')
    # Global
    config = {'font.family':'Times New Roman', 'figure.dpi':350, 'figure.figsize':(12.5,9), 'axes.labelsize':25}
    plt.rcParams.update(config)
    return None

# Color
def firefly():
    '''
    0. #3e324a（紫黑）
    1. #475d7b（灰蓝）
    2. #97c6c0（灰绿）
    3. #e26e1b（深橘黄）
    4. #4df8e8（蓝绿）
    5. #e6e4e0（银白）
    '''
    colors = ('#3e324a', '#475d7b', '#97c6c0', '#e26e1b', '#4df8e8', '#e6e4e0')
    return colors

# Standardized Plot
def std_plot(x, y, legend_name, plot_name='', x_label='X', y_label='Y', plot_type='curve'):
    '''
    '''
    plt.figure()
    if isinstance(y, tuple):
        for i in range(len(y)):
            if plot_type == 'curve':
                plt.plot(x, y[i], label=legend_name[i], color=firefly()[i])
            if plot_type == 'scatter':
                plt.scatter(x, y[i], label=legend_name[i], color=firefly()[i])
    else:
        if plot_type == 'curve':
            plt.plot(x, y, label=legend_name, color=firefly()[1])
        if plot_type == 'scatter':
            plt.scatter(x, y, label=legend_name, color=firefly()[1])
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(plot_name, fontsize=25)
    plt.legend(fontsize=20, frameon=True, shadow=True)
    plt.show()
    return None
