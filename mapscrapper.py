import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os

PAUSE_TIME = 5

def scroll_down():
    global driver
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            time.sleep(PAUSE_TIME)
            new_height = driver.execute_script("return document.body.scrollHeight")

            try:
                driver.find_element(By.CSS_SELECTOR, ".mye4qd").click()
            except:

               if new_height == last_height:
                   break


        last_height = new_height

locations = ['red sea', 'galapagos', 'palau', 'sipadan', 'saipan', 'maldives', 'koh tao', 'key largo', 'bohol', 'cebu', 'malapascua', 'el nido', 'sabang', 'lambongan island', 'lombok', 'komodo']

for location in locations:
    url = f"https://www.google.com/search?q={location} dive point site &source=lnms&tbm=isch&sa=X&ved=2ahUKEwjgwPKzqtXuAhWW62EKHRjtBvcQ_AUoAXoECBEQAw&biw=768&bih=712"

    service = Service('chromedriver/chromedriver')
    driver = webdriver.Chrome(service=service)
    driver.get(url)

    time.sleep(PAUSE_TIME)

    scroll_down()

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    images = soup.find_all('img', attrs={'class':'rg_i Q4LuWd'})

    print('number of img tags: ', len(images))

    n = 1
    for i in images:

        try:
            imgUrl = i["src"]
        except:
            imgUrl = i["data-src"]

        if not os.path.exists(f"maps/{location}"):
            os.makedirs(f"maps/{location}", exist_ok=True)
        try:
            with urllib.request.urlopen(imgUrl) as f:
                with open(f"maps/{location}/" + str(location) + '_' + str(n) + '.jpg', 'wb') as h:
                    img = f.read()
                    h.write(img)
        except:
            continue
        n += 1

    driver.quit()