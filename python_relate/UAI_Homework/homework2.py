import numpy as np
import matplotlib.pyplot as plt

# 设置中文字体，防止绘图乱码
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def forward_cloud_generator(Ex, En, He, n_drops):
    """
    正向正态云发生器
    :param Ex: 期望 (Expectation)
    :param En: 熵 (Entropy)
    :param He: 超熵 (Hyper-entropy)
    :param n_drops: 生成云滴的数量
    :return: 云滴数组
    """
    # 1. 生成随机熵 En'：以En为期望，He^2为方差的正态随机数
    En_prime = np.random.normal(loc=En, scale=He, size=n_drops)
    
    # 2. 生成云滴 x：以Ex为期望，En'^2为方差的正态随机数
    x = np.random.normal(loc=Ex, scale=np.abs(En_prime), size=n_drops)
    
    return x

def homework_2_visualization():
    """
    第二次作业：绘制二维云模型随超熵变化的动态情况
    """
    Ex = 0
    En = 1
    n_drops = 2000
    He_list = [0.1, 0.5, 1.0, 2.0] # 选取不同He值进行对比
    
    fig, axes = plt.subplots(2, 2, figsize=(10, 10))
    fig.suptitle('实验二：二维云模型随超熵(He)增加的云滴分布变化', fontsize=16)

    for i, He in enumerate(He_list):
        ax = axes[i // 2, i % 2]
        
        # 产生两个独立的云模型作为X和Y坐标
        x_drops = forward_cloud_generator(Ex, En, He, n_drops)
        y_drops = forward_cloud_generator(Ex, En, He, n_drops)
        
        # 绘制散点图
        ax.scatter(x_drops, y_drops, s=5, c='r', alpha=0.5)
        
        # 绘制核心层参考圆 (半径 En)
        circle = plt.Circle((Ex, Ex), En, color='blue', fill=False, linestyle='--')
        ax.add_patch(circle)
        
        ax.set_title(f'He = {He}')
        ax.set_xlim(-10, 10)
        ax.set_ylim(-10, 10)
        ax.set_aspect('equal', adjustable='box') # 保持XY轴比例一致
        ax.grid(True)

    plt.tight_layout()
    plt.show()

# 运行作业2
homework_2_visualization()