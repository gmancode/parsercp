from selenium import webdriver
import time #модуль для sleep[]
import random #модуль для использования user-agent в рандомном порядке
from fake_useragent import UserAgent



url = "https://magiceden.io/" #ссылка на сайт
#url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/" #ссылка на сайт

user_agents_list = [   #список user-agent чтоб тебя не заблокирроолвали можно сделать оидельным файлом чтоб не было каши
    "1",
    "2",
    "3"
]

useragent = UserAgent()

# options
options = webdriver.ChromeOptions()
#options.add_argument(f"user-agent={random.choice(user_agents_list)}") #здесь указываем либо user-agent конкретный либо список с функицей рандом
options.add_argument(f"user-agent={useragent.random}") #в данном случае исользуем библиотеку fake_useragent с параметром random

driver  =   webdriver.Chrome(
    executable_path="C:\\Users\\user\\Documents\\Python Project\\Project 1 test parser selenium\\chromedriver.exe", options=options ) #это драйвер точнее окно 
                                                                                                     #браузера c опцией user agent

try: #наши запросы 
    driver.get(url=url) #метод get для передачи url ссылки
    time.sleep(10) #время жизни бразуера в секундах
except Exception as ex: #вывод ошибок
    print(ex)
finally: #закрытие драйвера чтоб мог закрытьсяя всегда
    driver.close()
    driver.quit() 