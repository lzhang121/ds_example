from DrissionPage import Chromium

browser = Chromium()  # 创建浏览器对象
browser.set.retry_times(20)  # 设置整体运行参数
tab = browser.latest_tab  # 获取Tab对象
# 跳转到登录页面
tab.get('https://gitee.com/login#lang=zh-CN')

browser.quit()  # 关闭浏览器
