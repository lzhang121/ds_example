from DrissionPage import Chromium

# 启动或接管浏览器，并创建标签页对象
tab = Chromium().latest_tab
# 跳转到登录页面
tab.get('https://gitee.com/login#lang=zh-CN')

# 定位到账号文本框，获取文本框元素
ele = tab.ele('#user_login')
# 输入对文本框输入账号
ele.clear()
ele.input('zhanglei')
# 定位到密码文本框并输入密码
pwd = tab.ele('#user_password')
pwd.clear()
pwd.input('Gitee12345!')
# 点击登录按钮
tab.ele('@value=Sign in').click()
