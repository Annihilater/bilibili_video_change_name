# 介绍

> 本项目仅适用于Mac平台，使用Python 3.8开发

使用B站Windows客户端下载视频后是这个样子的：

![2021-03-28-19-47-57](https://klause-blog-pictures.oss-cn-shanghai.aliyuncs.com/uPic/2021-03-28-19-47-57.png)

视频的文件名都是数字，本项目旨在将视频文件名修改为正确的名称。

1. 从 `.info` 文件中提取出正确的视频文件名

2. 修改视频文件的名称

3. 将视频文件从子目录（图中类似于`1`、`2`、`3`...等的目录）移动到上级目录

4. 删除子目录内 `.xml` 文件和 `.info` 文件，再删除子目录

5. 修改视频文件夹的名称（类似于`415138740` 改为 `SpringCloud Netflix从入门到精通教程`等正确的教程目录）

# 使用方法

重要提示：使用前先做好备份，出现任何损失概不负责

1. 创建好Python3.8的虚拟环境

2. 克隆仓库

```Bash
git clone https://github.com/Annihilater/bilibili_video_change_name.git 
```

1. 修改视频目录路径

![2021-03-28-19-55-22](https://klause-blog-pictures.oss-cn-shanghai.aliyuncs.com/uPic/2021-03-28-19-55-22.png)

将上图标红部分替换为你本机（下载好的视频教程的文件夹）目录，然后运行 main.py 文件

1. 执行程序

```Bash
python main.py
```

# 效果展示

![2021-03-28-19-57-55](https://klause-blog-pictures.oss-cn-shanghai.aliyuncs.com/uPic/2021-03-28-19-57-55.png)