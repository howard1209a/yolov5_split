import os
import torch

# 创建保存目录
save_dir = 'sub_model_ptl'
os.makedirs(save_dir, exist_ok=True)

# 示例输入列表
example_input_list = [torch.randn(1, 3, 640, 640), torch.randn(1, 16, 320, 320), torch.randn(1, 32, 160, 160),
                      torch.randn(1, 32, 160, 160), torch.randn(1, 64, 80, 80), torch.randn(1, 64, 80, 80),
                      torch.randn(1, 128, 40, 40), torch.randn(1, 128, 40, 40), torch.randn(1, 256, 20, 20),
                      torch.randn(1, 256, 20, 20), torch.randn(1, 256, 20, 20), torch.randn(1, 128, 20, 20)]

for i in range(len(example_input_list)):
    model = torch.load("sub_model/sub_model" + str(i + 1) + ".pth")
    model.eval()  # 设置为评估模式
    traced_model = torch.jit.trace(model, example_input_list[i])
    traced_model.save(os.path.join(save_dir, f'sub_model{i + 1}.ptl'))
