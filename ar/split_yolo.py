import os
import torch
from models.experimental import attempt_load
import torch.nn as nn

# 加载 YOLOv5 模型
full_model = attempt_load('yolov5n.pt')

# 获取模型层
model_layers = full_model.model

# 确定每个子模型包含的层数
num_layers = len(model_layers)
num_splits = 25
layers_per_split = num_layers // num_splits

# 创建保存子模型的文件夹
save_dir = 'sub_model'
os.makedirs(save_dir, exist_ok=True)

# 保存每个子模型
for i in range(num_splits):
    start_index = i * layers_per_split
    # 如果是最后一个子模型，包含剩余的所有层
    end_index = (i + 1) * layers_per_split if i < num_splits - 1 else num_layers
    sub_model_layers = model_layers[start_index:end_index]

    # 封装为 nn.Sequential
    sub_model = nn.Sequential(*sub_model_layers)

    # 保存子模型
    torch.save(sub_model, os.path.join(save_dir, f'sub_model{i + 1}.pth'))
