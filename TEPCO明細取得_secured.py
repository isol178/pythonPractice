import time, os
from selenium import webdriver
import chromedriver_binary

user_id = "idHere"
password ="passwordHere"
download_dir = os.path.dirname(__file__)
opt = webdriver.ChromeOptions()
opt.add_experimental_option("prefs",{"download.default_directory": download_dir, "download.prompt_for_download": False,"plugins.always_open_pdf_externally":True})
driver = webdriver.Chrome(options=opt)

driver.get("https://www.kurashi.tepco.co.jp/pf/ja/pc/pub/site/logout.page")
time.sleep(3)
u = driver.find_element_by_name("ACCOUNTUID")
u.send_keys(user_id)
p = driver.find_element_by_name("PASSWORD")
p.send_keys(password)
p.submit()
time.sleep(3)

tag = driver.find_element_by_link_text("ご利用明細を確認する")
tag.click()
time.sleep(3)
tag = driver.find_element_by_link_text("グラフで見る")
href = tag.get_attribute("href")
driver.get(href)
time.sleep(3)

tag = driver.find_element_by_link_text("CSV形式でダウンロード")
href = tag.get_attribute("href")
driver.get(href)
time.sleep(10)

driver.quit()
