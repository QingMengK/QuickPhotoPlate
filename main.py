import subprocess
import time
import os
from io import BytesIO
from PIL import Image
import win32clipboard

# ================== 配置 ==================
ADB_PATH = "C:/platform-tools/adb.exe"  # 如果 adb 不在环境变量，改成绝对路径
REMOTE_DIR = "/sdcard/Pictures/Screenshots/"
LOCAL_FILE = "latest.png"

# ================== 剪贴板函数 ==================
def set_clipboard_image(image_path):
    image = Image.open(image_path)
    output = BytesIO()
    image.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:]  # 去掉 BMP header

    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    win32clipboard.CloseClipboard()

# ================== 获取最新截图 ==================
def get_latest_screenshot():
    try:
        result = subprocess.check_output(
            [ADB_PATH, "shell", "ls", "-t", REMOTE_DIR],
            stderr=subprocess.DEVNULL
        ).decode().splitlines()

        if result:
            return result[0]
    except:
        return None

    return None

# ================== 拉取文件 ==================
def pull_file(filename):
    remote_path = REMOTE_DIR + filename
    subprocess.run(
        [ADB_PATH, "pull", remote_path, LOCAL_FILE],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

# ================== 主循环 ==================
def main():
    print("=== 安卓截图同步到Windows剪贴板 ===")
    print("请确保：")
    print("1. 已开启USB调试")
    print("2. 已连接设备 (adb devices)")
    print("----------------------------------")

    last_file = None

    while True:
        filename = get_latest_screenshot()

        if filename and filename != last_file:
            print(f"检测到新截图: {filename}")

            pull_file(filename)

            if os.path.exists(LOCAL_FILE):
                try:
                    set_clipboard_image(LOCAL_FILE)
                    print("已复制到剪贴板 ✔")
                except Exception as e:
                    print("剪贴板写入失败:", e)

            last_file = filename

        time.sleep(1)

# ================== 启动 ==================
if __name__ == "__main__":
    main()