项目说明：

Wav2Lip :通过输入视频（视频中人物嘴尽量不要动）/图片，以及对应的音频，然后进行合成
但是输出的视频分辨率不高。

视频切帧：将Wav2Lip生成的分辨率不高的视频，切帧并保存到对应文件夹

GFPGAN：输入图片/包含图片的文件夹。对图片或文件夹中的图片批量处理，得到超分后的图片

视频合成：将超分后的图片文件合成高清视频（视频没有声音）

视频音频合成：将超分后合成的视频与音频结合，输出最终的视频文件。


虚拟环境配置：环境可以按照Wav2Lip的环境先进行配置，然后在这个环境的基础上安装GFPGAN对应缺少的包即可


参考项目：

https://github.com/Rudrabha/Wav2Lip

https://github.com/TencentARC/GFPGAN


权重文件：
链接：https://pan.baidu.com/s/1NO1PD6KxCeTy5G-RO9yFeQ 
提取码：b0bv

其中：s3fd.pth 放在face_detection/detection/sfd/s3fd.pth

GFPGANv1.3.pth 放在experiments/pretrained_models/GFPGANv1.3.pth

lipsync_expert.pth、visual_quality_disc.pth、wav2lip.pth、 wav2lip_gan.pth四个权重文件放在checkpoints/