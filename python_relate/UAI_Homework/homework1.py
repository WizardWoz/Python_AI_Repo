import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 设置中文字体
rcParams['font.sans-serif'] = ['SimHei']
rcParams['axes.unicode_minus'] = False

class NormalCloudGenerator:
    """正态云发生器"""
    
    def __init__(self, Ex, En, He, n=1000):
        """
        参数:
        Ex: 期望值，定性概念的中心值
        En: 熵，定性概念的不确定性度量
        He: 超熵，熵的不确定性度量
        n: 生成云滴数量
        """
        self.Ex = Ex
        self.En = En
        self.He = He
        self.n = n
        
    def generate_cloud_drops(self):
        """生成云滴"""
        # 生成熵的随机值
        En_prime = np.random.normal(self.En, self.He, self.n)
        # 生成云滴
        x = np.random.normal(self.Ex, np.abs(En_prime), self.n)
        # 计算确定度
        y = np.exp(-(x - self.Ex)**2 / (2 * En_prime**2))
        
        return x, y
    
    def plot_cloud(self, ax, title="", color='blue'):
        """绘制云图"""
        x, y = self.generate_cloud_drops()
        
        # 绘制云滴
        scatter = ax.scatter(x, y, c=color, alpha=0.6, s=10, label=title)
        ax.set_xlabel('数值 x')
        ax.set_ylabel('确定度 μ(x)')
        ax.set_title(title)
        ax.grid(True, alpha=0.3)
        ax.set_ylim(0, 1.1)
        
        return scatter

def compare_parameters():
    """对比不同参数下的云图变化"""
    fig, axes = plt.subplots(2, 3, figsize=(18, 12))
    fig.suptitle('正态云模型参数对比分析', fontsize=16, fontweight='bold')
    
    # 基准参数
    base_Ex, base_En, base_He = 0, 1, 0.1
    
    # 1. 改变期望值 Ex
    Ex_values = [-2, 0, 2]
    for i, Ex in enumerate(Ex_values):
        cloud = NormalCloudGenerator(Ex, base_En, base_He)
        cloud.plot_cloud(axes[0, i], f'Ex={Ex}, En={base_En}, He={base_He}', 'red')
    
    # 2. 改变熵 En
    En_values = [0.5, 1, 2]
    for i, En in enumerate(En_values):
        cloud = NormalCloudGenerator(base_Ex, En, base_He)
        cloud.plot_cloud(axes[1, i], f'Ex={base_Ex}, En={En}, He={base_He}', 'green')
    
    plt.tight_layout()
    plt.show()

def compare_he_parameter():
    """专门对比超熵 He 的影响"""
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    fig.suptitle('超熵(He)对云模型的影响', fontsize=16, fontweight='bold')
    
    He_values = [0.05, 0.2, 0.5]
    colors = ['blue', 'orange', 'red']
    
    for i, (He, color) in enumerate(zip(He_values, colors)):
        cloud = NormalCloudGenerator(0, 1, He, n=2000)
        cloud.plot_cloud(axes[i], f'Ex=0, En=1, He={He}', color)
    
    plt.tight_layout()
    plt.show()

def practical_examples():
    """实际概念示例"""
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('云模型在实际概念表示中的应用', fontsize=16, fontweight='bold')
    
    # 1. "年轻人"概念
    young_cloud = NormalCloudGenerator(Ex=25, En=5, He=0.5, n=1500)
    young_cloud.plot_cloud(axes[0, 0], '概念: "年轻人"\n(年龄分布)', 'skyblue')
    axes[0, 0].set_xlabel('年龄')
    
    # 2. "天气热"概念
    hot_cloud = NormalCloudGenerator(Ex=30, En=3, He=0.3, n=1500)
    hot_cloud.plot_cloud(axes[0, 1], '概念: "天气热"\n(温度分布)', 'red')
    axes[0, 1].set_xlabel('温度(℃)')
    
    # 3. "中等身高"概念
    height_cloud = NormalCloudGenerator(Ex=170, En=8, He=0.4, n=1500)
    height_cloud.plot_cloud(axes[1, 0], '概念: "中等身高"\n(身高分布)', 'green')
    axes[1, 0].set_xlabel('身高(cm)')
    
    # 4. "合适的价格"概念
    price_cloud = NormalCloudGenerator(Ex=100, En=20, He=0.6, n=1500)
    price_cloud.plot_cloud(axes[1, 1], '概念: "合适的价格"\n(价格分布)', 'purple')
    axes[1, 1].set_xlabel('价格(元)')
    
    plt.tight_layout()
    plt.show()

def cloud_vs_fuzzy_random():
    """对比云模型与模糊集、纯随机方法"""
    np.random.seed(42)
    
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    fig.suptitle('云模型 vs 模糊集 vs 纯随机方法', fontsize=16, fontweight='bold')
    
    # 1. 模糊集方法 (确定性隶属度)
    x_fuzzy = np.linspace(-3, 3, 100)
    y_fuzzy = np.exp(-x_fuzzy**2 / 2)  # 高斯隶属函数
    axes[0].plot(x_fuzzy, y_fuzzy, 'b-', linewidth=2, label='模糊隶属度')
    axes[0].set_title('模糊集方法\n(确定性隶属度)')
    axes[0].set_xlabel('x')
    axes[0].set_ylabel('μ(x)')
    axes[0].grid(True, alpha=0.3)
    axes[0].legend()
    
    # 2. 纯随机方法
    x_random = np.random.normal(0, 1, 1000)
    y_random = np.random.uniform(0, 1, 1000)
    axes[1].scatter(x_random, y_random, c='red', alpha=0.6, s=10)
    axes[1].set_title('纯随机方法\n(无规律)')
    axes[1].set_xlabel('x')
    axes[1].set_ylabel('随机值')
    axes[1].grid(True, alpha=0.3)
    
    # 3. 云模型方法
    cloud = NormalCloudGenerator(Ex=0, En=1, He=0.1, n=1000)
    x_cloud, y_cloud = cloud.generate_cloud_drops()
    axes[2].scatter(x_cloud, y_cloud, c='green', alpha=0.6, s=10)
    axes[2].set_title('云模型方法\n(随机性与模糊性结合)')
    axes[2].set_xlabel('x')
    axes[2].set_ylabel('确定度 μ(x)')
    axes[2].grid(True, alpha=0.3)
    
    for ax in axes:
        ax.set_ylim(0, 1.1)
    
    plt.tight_layout()
    plt.show()

def analyze_cloud_characteristics():
    """分析云模型的数学特性"""
    # 生成大量云滴进行统计分析
    cloud = NormalCloudGenerator(Ex=0, En=1, He=0.2, n=10000)
    x, y = cloud.generate_cloud_drops()
    
    print("云模型统计特性分析:")
    print(f"云滴数量: {len(x)}")
    print(f"x的均值: {np.mean(x):.3f} (接近Ex=0)")
    print(f"x的标准差: {np.std(x):.3f}")
    print(f"确定度y的均值: {np.mean(y):.3f}")
    print(f"确定度y的标准差: {np.std(y):.3f}")
    
    # 绘制分布直方图
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    ax1.hist(x, bins=50, density=True, alpha=0.7, color='blue')
    ax1.set_title('云滴x值的分布')
    ax1.set_xlabel('x值')
    ax1.set_ylabel('密度')
    ax1.grid(True, alpha=0.3)
    
    ax2.hist(y, bins=50, density=True, alpha=0.7, color='red')
    ax2.set_title('确定度μ(x)的分布')
    ax2.set_xlabel('确定度μ(x)')
    ax2.set_ylabel('密度')
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    print("=== 正态云发生器演示 ===")
    
    # 1. 基本云图
    print("\n1. 基本正态云图")
    fig, ax = plt.subplots(figsize=(10, 6))
    base_cloud = NormalCloudGenerator(Ex=0, En=1, He=0.1)
    base_cloud.plot_cloud(ax, "基本正态云模型 (Ex=0, En=1, He=0.1)")
    plt.show()
    
    # 2. 参数对比
    print("\n2. 参数对比分析")
    compare_parameters()
    compare_he_parameter()
    
    # 3. 实际应用示例
    print("\n3. 实际概念表示")
    practical_examples()
    
    # 4. 方法对比
    print("\n4. 与其他方法对比")
    cloud_vs_fuzzy_random()
    
    # 5. 统计分析
    print("\n5. 云模型统计特性")
    analyze_cloud_characteristics()