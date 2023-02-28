import io
import base64
from PIL import ImageGrab, Image

# 读取剪贴板中的图像数据
img = ImageGrab.grabclipboard()

if img is not None:
    # 将图像转换为 JPEG 格式，压缩质量为 75%
    output = io.BytesIO()
    img.convert('RGB').save(output, 'JPEG', quality=75)

    # 将 JPEG 数据转换为 base64 编码的字符串
    b64_data = base64.b64encode(output.getvalue()).decode('utf-8')

    # 输出 base64 编码的字符串
    print(b64_data)
