import time, os, requests
from selenium import webdriver
import chromedriver_binary

#パスワードの指定
user_id = "test"
password = "pwpw"
download_dir = os.path.dirname(__file__)
#保存先などオプションで指定してChromeを起動
opt = webdriver.ChromeOptions()
opt.add_experimental_option("prefs",{"download.default_directory": download_dir, "download.prompt_for_download": False,"plugins.always_open_pdf_externally":True})
driver = webdriver.Chrome(options=opt)
#カード会社のページを開く
driver.get('https://kujirahand.com/sample/dummy-card/')
time.sleep(3)
#ログインページを開く
tag = driver.find_element_by_link_text('ログイン')
tag.click()

u = driver.find_element_by_name('username_mmlbbs6')
u.send_keys(user_id)

p = driver.find_element_by_name('password_mmlbbs6')
p.send_keys(password)
p.submit()
time.sleep(3)

tag = driver.find_element_by_link_text('今月の明細')
tag.click()

tag = driver.find_element_by_link_text('*ダウンロード*')
href = tag.get_attribute('href')
tag.click()

#c = {}
#for cookie in driver.get_cookies():
#    c[cookie['name']] = cookie['value']

#r = requests.get(href, cookies=c)
#with open("data.csv", 'wb') as f:
#    f.write(r.content)

time.sleep(30)
driver.quit()
