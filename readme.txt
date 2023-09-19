项目说明：

1）Wav2Lip :通过输入视频（视频中人物嘴尽量不要动）/图片，以及对应的音频，然后进行合成
但是输出的视频分辨率不高。

2）视频切帧：将Wav2Lip生成的分辨率不高的视频，切帧并保存到对应文件夹

3）GFPGAN：输入图片/包含图片的文件夹。对图片或文件夹中的图片批量处理，得到超分后的图片

4）视频合成：将超分后的图片文件合成高清视频（视频没有声音）

5）视频音频合成：将超分后合成的视频与音频结合，输出最终的视频文件。


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


注意：该项目在运行过程中涉及的文件路径较多，容易混淆。
input文件夹中放置 图片/无声视频 和 音频。
output文件夹包含以上五步中产生的所有输出文件。
          Wav2Lip_results是第一次产生的分辨率较低的视频。
          qiezhen_result是对Wav2Lip生成的视频进行切帧后的图片。
          gfpgan_result是对qiezhen_result的图片进行超清处理后得到的高清图片。其中有四个文件夹对应保存的是不同的图片。下面合成视频时使用的是restored_imgs文件夹下的图片。
          hecheng_result是将restored_imgs中的图片合成无声的高清视频。
          final_result是最终输出的结果。

其中视频切帧，视频合成，音频视频合成的python代码在my_test中。如果运行时报错路径问题，文件不存在问题都可以单独运行代码进行测试。
inference.py是Wav2Lip的推理代码可单独执行
inference_gfpgan.py是GFPGAN的推理代码也可单独执行
my_inference.py是合并上面内容的推理代码，当文件及路径都设置正确后可一键生成高清视频。
