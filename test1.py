import os

def count_images_in_liver_dir(base_dir):
    # 获取 Task03_Liver_256 目录下的所有文件夹
    liver_dirs = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]

    total_images = 0
    # 遍历每个 liver_x 文件夹
    for liver_dir in liver_dirs:
        liver_path = os.path.join(base_dir, liver_dir)
        
        # 统计该文件夹下所有 jpg 文件的数量
        jpg_files = [f for f in os.listdir(liver_path) if f.endswith('.jpg')]
        
        # 更新总图片数
        total_images += len(jpg_files)
        
        # 打印每个文件夹的统计信息
        print(f"{liver_dir}: {len(jpg_files)} images")

    print(f"Total images across all liver_x folders: {total_images}")

# 示例路径
base_dir = "/mnt/data/huangyifei/segment-anything-2/videos/Brats2020" #18716
count_images_in_liver_dir(base_dir)
