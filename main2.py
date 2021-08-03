import time, telebot, requests, config
from bs4 import BeautifulSoup

bot = telebot.TeleBot(config.TOKEN)
page = 1
channel = '@igronovosti_tizeri'

while True:
    domain = f"https://avatarko.ru/kartinki/kot/{page}"
    responce = requests.get(domain).text

    all_image = BeautifulSoup(responce, 'lxml').find_all('div', class_= 'position-relative')

    for image in all_image:
        storage_url = image.find('a').get('href')
        print('1')
        if storage_url != '#':
            image = requests.get(storage_url).text
            result_link = BeautifulSoup(image, 'lxml').find('div', id='image_wrapper').find('img').get('src')
            image_bytes = requests.get(f"https://avatarko.ru{result_link}").content
            print('2')
            bot.send_photo(channel, image_bytes)
            time.sleep(int(3))
