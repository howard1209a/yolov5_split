import os
from PIL import Image

# 定义文件夹路径
origin_folder = 'images/origin'
processed_folder = 'images/processed'

# 创建 processed 文件夹（如果不存在）
os.makedirs(processed_folder, exist_ok=True)

# 获取 origin 文件夹中的所有图片文件
image_files = [f for f in os.listdir(origin_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

# 遍历图片文件并进行缩放
for index, image_file in enumerate(image_files, start=1):
    # 打开图像
    img_path = os.path.join(origin_folder, image_file)
    img = Image.open(img_path)

    # 缩放图像
    img_resized = img.resize((640, 640))

    # 保存处理后的图像
    output_filename = f'img{index}.jpg'
    output_path = os.path.join(processed_folder, output_filename)
    img_resized.save(output_path)

    print(f'Saved: {output_path}')

print('All images processed successfully!')
