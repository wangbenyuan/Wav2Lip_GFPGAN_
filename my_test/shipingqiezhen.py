import cv2
import os

# video_path = "D://python_code//GFPGAN-master//my_test//2.mp4"  # 视频文件路径
output_dir = "D://python_code//Wav2Lip-GFPGAN//output//qiezhen_result"  # 输出帧的目录

# 获得视频的帧率
def get_video_fps(video_path):
    # 打开视频文件
    video = cv2.VideoCapture(video_path)

    # 获取帧率
    fps = video.get(cv2.CAP_PROP_FPS)
    print(f"视频的帧率为: {fps} FPS")
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    print("总帧数：",total_frames)

    # 释放视频对象
    video.release()

    return fps

# 视频按帧切分成图片
def video_to_frames(video_path, output_dir):
    # 创建输出目录
    os.makedirs(output_dir, exist_ok=True)
    # 打开视频文件
    video = cv2.VideoCapture(video_path)
    # 获取帧率和总帧数
    fps = video.get(cv2.CAP_PROP_FPS)
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    # 计算每秒取多少帧
    frame_interval = int(fps / 24)  # 每秒XXX帧
    # 初始化帧计数器和图片计数器
    frame_count = 0
    image_count = 0
    # 循环读取视频帧
    while True:
        success, frame = video.read()
        if not success:
            break
        # 如果达到指定的帧间隔，则保存为图片
        if frame_count % frame_interval == 0:
            output_path = os.path.join(output_dir, f"frame_{image_count:06d}.jpg")
            cv2.imwrite(output_path, frame)
            image_count += 1
        frame_count += 1
    # 释放视频对象
    video.release()
    print(f"成功将视频切分成 {image_count} 张图片。")
# if __name__ == '__main__':
#     # 获取视频帧
#     # fps = get_video_fps(video_path)
#     # 将视频按帧切分
#     video_to_frames(video_path, output_dir)

