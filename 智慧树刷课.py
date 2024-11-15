from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager  # 如果你用 webdriver-manager 自动下载 chromedriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import winsound
from os import system as clr
def cl(x):#点击
    dr.execute_script("arguments[0].click();", x)
def t(x):#获取文本
    return dr.execute_script("return arguments[0].innerText;", x)
def q():#清屏
    clr('cls')
s=time.sleep
with open('user.txt','r') as f:
    user = f.read()
options = webdriver.ChromeOptions()
options.add_argument(f"user-data-dir=C:/Users/{user}/AppData/Local/Google/Chrome/User Data")
driver_path ='chromedriver-win64\chromedriver.exe'  
service = Service(driver_path)
dr = webdriver.Chrome(service=service,options=options)
actions = ActionChains(dr)
# driver.minimize_window()
url2='https://passport.zhihuishu.com/login?service=https://onlineservice-api.zhihuishu.com/gateway/f/v1/login/gologin'
url= 'https://www.zhihuishu.com/'
dr.get(url2)
def dd():
    try:
        p = dr.find_element(By.CLASS_NAME, 'playButton')
        p.click()
        return True
    except:
        return False

q()
try:
    cl(dr.find_element(By.XPATH,'/html/body/div[9]/div[1]/div[2]'))
except:
    print('无需登录')

input('调倍速至0.07(最低),进入视频页面回车')
q()
a = dr.find_elements(By.CLASS_NAME ,'catalogue_title')
ci=0
for i in a:
    print(ci,':',i.text)
    ci+=1
hao=int(input('当前视频序号：'))
q()
while(1):
    s(10)
    try:
        dd()
        print(f'{hao}/{len(a)}','视频进度:',dr.execute_script("return arguments[0].innerText;", dr.find_element(By.XPATH,'//li/div/div/div/span')))
    except:
        try:
            hao+=1
            if hao>len(a)-1:
                break
            a[hao].click()
            p = WebDriverWait(dr, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'playButton')))
            p.click()
            print('切换成功')
            winsound.Beep(1000, 200)
            s(3)
        except:
            continue
q()
print('全勾八刷完了')
winsound.Beep(1000, 200)
winsound.Beep(1000, 200)
winsound.Beep(1000, 200)
winsound.Beep(1000, 200)
winsound.Beep(1000, 200)
winsound.Beep(1000, 200)
s(11111)

#//*[@id="app"]/div/div[2]/div[2]/div[2]/div[1]/div/ul[3]/div[1] /li/div/div/div/span
#nextButton


