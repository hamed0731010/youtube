from pytube import YouTube
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

cservise=webdriver.ChromeService(executable_path='/home/hamed/Downloads/chromedriver/chromedriver')
driver=webdriver.Chrome(service=cservise)
def download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")


driver.get('https://www.youtube.com/watch?v=NfZPJc7zRM0&list=PLVN7DLFGYaP46oDpQtSnOR6vguu_YpUM9')
try:
    button=driver.find_element(By.CLASS_NAME,'yt-core-attributed-string yt-core-attributed-string--white-space-no-wrap').click()
except:
    print('no button')
time.sleep(5)
tags=driver.find_elements(By.TAG_NAME,"ytd-playlist-panel-video-renderer")
for tag in tags:
    path=tag.find_element(By.ID,'wc-endpoint').get_attribute('href')
    download(path)
#time.sleep(10)
driver.quit()