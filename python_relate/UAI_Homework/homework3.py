import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def forward_cloud_generator(Ex, En, He, n_drops):
    """
    正向正态云发生器 (同实验二)
    """
    En_prime = np.random.normal(loc=En, scale=He, size=n_drops)
    x = np.random.normal(loc=Ex, scale=np.abs(En_prime), size=n_drops)
    return x

def homework_3_statistics():
    """
    第三次作业：统计云滴分布随超熵变化的情况
    """
    Ex = 0
    En = 1
    n_drops = 1000  # 每次生成的云滴数
    He_steps = np.arange(0, 5.0, 0.05) # He变化范围，为清晰展示效果取[0, 5]，原要求是[0, 50]
    repeat_count = 50 # 外层循环次数（原要求1000，这里取50以加快运行）
    windows_coeffs = [0.618, 1.0, 2.0, 3.0] # 窗口系数 k，窗口为 [-k*En, k*En]
    
    # 初始化存储数组
    ratio_results = np.zeros((len(He_steps), len(windows_coeffs)))
    density_results = np.zeros((len(He_steps), len(windows_coeffs)))
    
    print(f"开始计算实验三指标 (He范围: 0-{He_steps[-1]:.2f}, 重复次数: {repeat_count})...")

    # 蒙特卡洛模拟求平均
    for r in range(repeat_count):
        temp_ratios = []
        temp_densities = []
        
        for He in He_steps:
            drops = forward_cloud_generator(Ex, En, He, n_drops)
            current_r_ratios = []
            current_r_densities = []
            
            for k in windows_coeffs:
                window_width = 2 * k * En
                limit = k * En
                
                # 统计落在窗口 [-limit, limit] 内的个数
                count = np.sum((drops >= Ex - limit) & (drops <= Ex + limit))
                
                # 计算比例 (%)
                ratio = (count / n_drops) * 100
                current_r_ratios.append(ratio)
                
                # 计算云心密度 = 个数 / 窗口宽度
                density = count / window_width
                current_r_densities.append(density)
            
            temp_ratios.append(current_r_ratios)
            temp_densities.append(current_r_densities)
            
        # 累加结果
        ratio_results += np.array(temp_ratios)
        density_results += np.array(temp_densities)

    # 求平均
    ratio_results /= repeat_count
    density_results /= repeat_count
    
    # --- 绘图 (图3) ---
    plt.figure(figsize=(10, 6))
    colors = ['k', 'b', 'r', 'm']
    for idx, k in enumerate(windows_coeffs):
        plt.plot(He_steps, ratio_results[:, idx], color=colors[idx], label=f"窗口 $\pm {k}En$")
    
    plt.title('图3: 落在窗口内的云滴个数与云滴总数比例变化情况')
    plt.xlabel('超熵 He')
    plt.ylabel('百分比 (%)')
    plt.legend()
    plt.grid(True, which='both', linestyle='--', alpha=0.7)
    plt.show()

    # --- 绘图 (图4) ---
    plt.figure(figsize=(10, 6))
    for idx, k in enumerate(windows_coeffs):
        plt.plot(He_steps, density_results[:, idx], color=colors[idx], label=f"云心密度 $\pm {k}En$")
    
    # 绘制云滴平均密度作为参考 (假设论域范围为20)
    avg_density = n_drops / 20.0
    plt.plot(He_steps, np.ones_like(He_steps) * avg_density, color='g', linestyle='--', label='云滴平均密度 (固定)')
    
    plt.title('图4: 云心密度随He增大的变化情况')
    plt.xlabel('超熵 He')
    plt.ylabel('密度')
    plt.legend()
    plt.grid(True, which='both', linestyle='--', alpha=0.7)
    plt.show()

# 运行作业3
homework_3_statistics()