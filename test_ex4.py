from DrissionPage import Chromium
browser = Chromium()
tab = browser.latest_tab
tab.get('https://DrissionPage.cn')
ele = tab.ele('text=文档')  # 获取文本为“文档”的元素
ele.click()  # 点击该元素
browser.quit()  # 关闭浏览器
