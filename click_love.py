from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--disable-application-cache")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--headless")  # 无头模式
chrome_options.add_argument("--no-sandbox")  # 禁用沙盒
chrome_options.add_argument("--disable-dev-shm-usage")  # 解决共享内存问题

# 初始化浏览器
driver = webdriver.Chrome(options=chrome_options)

try:
    driver.set_page_load_timeout(10)
    print('开始加载页面')
    driver.get("https://faculty.hzau.edu.cn/zhouxionghui/zh_CN/index.htm")
    
    
    
except Exception as e:
    print(e)
    print('页面仍在加载，手动停止加载')
    driver.execute_script('window.stop()')  # 手动停止页面加载

# 找到目标元素
element = driver.find_element(By.CSS_SELECTOR, '#_parise_imgobj_u10')

for _ in range(100000000):
    ActionChains(driver).move_to_element(element).click().perform()
    print('click  ' +  str(_))
    # 清除 cookies
    driver.delete_all_cookies()

# 关闭浏览器
driver.quit()
