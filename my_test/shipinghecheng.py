import cv2
import os

# input_images_folder = 'D://python_code//Wav2Lip-GFPGAN//output//gfpgan_result//restored_imgs'
# output_video_file = 'D://python_code//Wav2Lip-GFPGAN//output//hencheng_result//fine.mp4'

def images_to_video(input_images_folder, output_video_file, frame_rate=30):
    # 获取图片列表

    # 获取图片列表
    image_files = [os.path.join(input_images_folder, f) for f in os.listdir(input_images_folder) if f.endswith('.jpg')]

    # 获取第一张图片的宽度和高度
    frame = cv2.imread(image_files[0])
    height, width, layers = frame.shape

    # 使用VideoWriter对象创建视频文件
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_video_file, fourcc, 29, (width, height))

    # 逐帧将图片写入视频
    for image_file in image_files:
        frame = cv2.imread(image_file)
        out.write(frame)

    # 完成后释放资源
    out.release()
    cv2.destroyAllWindows()

# 调用函数并传入参数

# images_to_video(input_images_folder, output_video_file)
