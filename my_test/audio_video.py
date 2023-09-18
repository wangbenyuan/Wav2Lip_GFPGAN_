from moviepy.editor import VideoFileClip, AudioFileClip

# audio_file = 'D://python_code//Wav2Lip-GFPGAN//input//audio.wav'
# video_file = 'D://python_code//Wav2Lip-GFPGAN//output//hecheng_result//fine.mp4'
def audio_video(audio_file, video_file):
    # 读取视频和音频文件
    video_clip = VideoFileClip(video_file)
    audio_clip = AudioFileClip(audio_file)

    # 将音频添加到视频中
    video_clip = video_clip.set_audio(audio_clip)

    # 输出合并后的视频文件
    output_file = 'D://python_code//Wav2Lip-GFPGAN//output//final_result//output_video_with_audio.mp4'
    video_clip.write_videofile(output_file, codec='libx264')

    # 关闭视频和音频文件的资源
    video_clip.close()
    audio_clip.close()

# audio_video(audio_file, video_file)