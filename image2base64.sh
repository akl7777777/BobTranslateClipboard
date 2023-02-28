#!/bin/zsh

# 从剪贴板中提取PNG格式的图片数据，并将其编码为Base64字符串
IMAGE_DATA=$(pngpaste - | base64)

# 将编码后的Base64字符串复制到剪贴板中
echo $IMAGE_DATA | pbcopy

# 在终端中输出编码后的Base64字符串
echo $IMAGE_DATA
