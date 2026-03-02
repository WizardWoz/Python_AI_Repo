import tensorflow as tf

# 检查GPU是否可用
print("TensorFlow版本:", tf.__version__)
print("GPU设备列表:", tf.config.list_physical_devices('GPU'))
print("是否检测到GPU:", len(tf.config.list_physical_devices('GPU')) > 0)

# 如果是ROCm版本的TensorFlow，应该能看到AMD GPU
if tf.config.list_physical_devices('GPU'):
    gpu = tf.config.list_physical_devices('GPU')[0]
    print("GPU信息:", gpu)