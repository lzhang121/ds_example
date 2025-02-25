from DrissionPage import Chromium

tab = Chromium().latest_tab
tab.screencast.set_save_path('video')  # 设置视频存放路径
tab.screencast.set_mode.video_mode()  # 设置录制
tab.screencast.start()  # 开始录制
tab.wait(3)
tab.screencast.stop()  # 停止录制
