# Photo plate Between Android and Windows
# 基于ADB实现安卓设备截图并保存到Windows电脑剪切板
## 食用方法

首先你需要一根数据线，一台Windows笔记本,以及一台安卓设备
- 1.安装python
- 2.安装adb
[adb网址]http://developer.android.com/tools/releases/platform-tools?hl=zh-cn

解压后将 main.py 第九行的ADB_PATH 改成adb.exe的绝对地址
- 3.安装依赖:
```shell
python -m pip install pywin32
```
```shell
python -m pip install pillow
```
- 4.运行：
```shell
python main.py  
```
