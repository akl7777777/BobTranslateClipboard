# BobTranslateClipboard
### bob直接调用系统剪切板翻译图片的AlfredWorkflow

### 无需Alfred也能快捷键调用脚本了

使用前环境: 1.有Python3的运行 /usr/bin/pip3 install pillow 完成后即可开始使用

苹果原生下载地址:[Bob.workflow-apple.zip](https://github.com/akl7777777/BobTranslateClipboard/releases/download/v0.0.1/Bob.workflow-apple.zip)

使用方法:
1.双击安装
2.打开服务,找到通用,设置快捷键如下图:
<img width="670" alt="image" src="https://user-images.githubusercontent.com/84266551/222150342-d38452c0-7c18-4486-b4ae-5b02f93bf80a.png">



![image](https://user-images.githubusercontent.com/84266551/222148759-6cd395f2-318c-4ce4-b4a5-2ea8e968102f.png)

#### 社区版Bob的福音,也能用了

按照下面的步骤配置一下:

>1.打开apple压缩包,解压后有一个自动操作文件,先不要双击它;

>2.找到你电脑里面的自动操作app并打开

>3.菜单栏选择文件->打开...->找到刚刚下载解压的自动文件打开

>4.在运行shell脚本的框中粘贴这段代码[apple_for_bob_community.py](https://github.com/akl7777777/BobTranslateClipboard/blob/main/apple_for_bob_community.py)

(**注意:代码中的ak和sk需要自行去火山官网申请,然后在代码中替换成自己的;**[申请教程](https://bobtranslate.com/service/ocr/volcengine.html)见Bob官网)

>5.保存即可开始使用,跟商店版使用方式相同

### bob翻译插件大合集:

>[DeepL翻译插件(免秘钥)](https://github.com/akl7777777/bob-plugin-akl-deepl-free-translate)

>[有道翻译插件(免秘钥)](https://github.com/akl7777777/bob-plugin-akl-youdao-free-translate)

>[火山翻译插件(免秘钥)](https://github.com/akl7777777/bob-plugin-akl-volcengine-free-translate)

>[腾讯翻译君插件(免秘钥)](https://github.com/akl7777777/bob-plugin-akl-tencent-free-translate)

>[腾讯交互翻译插件(免秘钥)](https://github.com/akl7777777/bob-plugin-akl-transmart-free-translate)

>[百度翻译插件(免秘钥)](https://github.com/akl7777777/bob-plugin-akl-baidu-free-translate)

>[彩云小译插件(免秘钥)](https://github.com/akl7777777/bob-plugin-akl-caiyunxiaoyi-free-translate)

>[只为日语 - MOJi辞書（じしょ）](https://github.com/akl7777777/bob-plugin-akl-mojidict-translate)

>[Bob翻译剪切板图片的AlfredWorkflow](https://github.com/akl7777777/BobTranslateClipboard)


当你用bob识图翻译的时候,是否遇到过这种尴尬的情况:

浏览网页时,突然发现一张有趣的图,想截图通过聊天软件发给便宜,或者是直接复制网页图片发给朋友;发了之后才突然想起来,原来图片上有写外语不认识,好想翻译一下,但是又不想去聊天记录里面重新截取一遍;没错,这就是我的痛点,所以我弄了这个Alfred Workflow

安装工作流需要你有[Bob](https://bobtranslate.com/)(一款 macOS 平台翻译和 OCR 软件)和[Alfred](https://www.alfredapp.com/)(Alfred是一款屡获殊荣的macOS应用程序，可通过热键、关键字、文本扩展等提高您的效率。搜索您的Mac和网络，并通过自定义操作来控制您的Mac以提高工作效率。)

安装方式:点击[BobTranslateClipboard_v0.0.1.alfredworkflow](https://github.com/akl7777777/BobTranslateClipboard/releases/download/v0.0.1/BobTranslateClipboard_v0.0.1.alfredworkflow)下载双击直接导入Alfred

使用前环境:
1.有Python3的运行
/usr/bin/pip3 install pillow
完成后即可开始使用

2.没有Python的运行
brew install pngpaste
完成后把工作流的Python连线断开,把zsh连线连上就可以使用了,如下图:
<img width="621" alt="image" src="https://user-images.githubusercontent.com/84266551/221875258-6b85790b-fbe3-41cd-b2af-2e626bf6a937.png">



使用方法:

快捷键⌥option+v 直接识别剪切板翻译

效果如下:

![iShot_2023-02-28_21 43 54](https://user-images.githubusercontent.com/84266551/221872349-5a738976-542d-4fbd-8de5-731f12b2a6ee.gif)


最后感谢大家对我开发插件的认可



### 开发不易,如果喜欢可以请作者喝一杯可乐,谢谢!


![image](https://user-images.githubusercontent.com/84266551/219829283-3ed1798e-aeed-4174-bbcb-f93bf3008817.png)

