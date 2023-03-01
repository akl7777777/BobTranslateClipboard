import io
import base64
from PIL import ImageGrab, Image
import subprocess

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

    script = '''
	    -- 以下为辅助方法，必须写在脚本最外层头部
        use scripting additions
        use framework "Foundation"
        on callBob(recordValue)
	    set theParameter to (((current application's NSString)'s alloc)'s initWithData:((current application's NSJSONSerialization)'s dataWithJSONObject:recordValue options:1 |error|:(missing value)) encoding:4) as string
	    tell application id "com.hezongyidev.Bob" to request theParameter
        end callBob

        -- 以下为调用 Bob 的参数，仅需修改这部分代码
        callBob({|path|:"translate", body:{action:"translateImage", imageBase64:"%s"}})
	''' % b64_data
    process = subprocess.Popen(["osascript", "-e", script])
