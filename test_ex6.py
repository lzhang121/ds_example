from DrissionPage import Chromium

browser = Chromium()
tab1 = browser.latest_tab
tab2 = browser.latest_tab

tab1.get('https://DrissionPage.cn')
tab2.get('https://www.baidu.com')

browser.quit()
