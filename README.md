# BobTranslateClipboard
### bob直接调用系统剪切板翻译图片的AlfredWorkflow

当你用bob识图翻译的时候,是否遇到过这种尴尬的情况:

浏览网页时,突然发现一张有趣的图,想截图通过聊天软件发给便宜,或者是直接复制网页图片发给朋友;发了之后才突然想起来,原来图片上有写外语不认识,好想翻译一下,但是又不想去聊天记录里面重新截取一遍;没错,这就是我的痛点,所以我弄了这个Alfred Workflow

安装工作流需要你有[Bob](https://bobtranslate.com/)(一款 macOS 平台翻译和 OCR 软件)和[Alfred](https://www.alfredapp.com/)(Alfred是一款屡获殊荣的macOS应用程序，可通过热键、关键字、文本扩展等提高您的效率。搜索您的Mac和网络，并通过自定义操作来控制您的Mac以提高工作效率。)

安装方式:点击[BobTranslateClipboard_v0.0.1.alfredworkflow](https://github.com/akl7777777/BobTranslateClipboard/releases/download/v0.0.1/BobTranslateClipboard_v0.0.1.alfredworkflow)下载双击直接导入Alfred

使用前环境:
1.有Python3的运行
/usr/bin/pip3 install Pillow
完成后即可开始使用

2.没有Python的运行
brew install pngpaste
完成后把工作流的Python连线断开,把zsh连线连上就可以使用了,如下图:
<img width="621" alt="image" src="https://user-images.githubusercontent.com/84266551/221875258-6b85790b-fbe3-41cd-b2af-2e626bf6a937.png">



使用方法:

快捷键⌥option+v 直接识别剪切板翻译

效果如下:

![iShot_2023-02-28_21 43 54](https://user-images.githubusercontent.com/84266551/221872349-5a738976-542d-4fbd-8de5-731f12b2a6ee.gif)



