from detect import run
def main():
    # 设置参数
    weights = 'yolov5s.pt'  # 模型权重
    source = '/Users/howard1209a/Desktop/codes/yolov5/data/images/bus.jpg'      # 输入图像文件
    # conf_thres = 0.25       # 置信度阈值
    # iou_thres = 0.45        # NMS IOU阈值
    # save_img = True         # 是否保存结果图像

    # 调用推理函数
    run(weights=weights, source=source)

if __name__ == '__main__':
    main()
