import telebot
import feedparser
import time
import config
import ssl
from telebot import types
from datetime import datetime
from time import mktime

ssl._create_default_https_context = ssl._create_unverified_context
bot = telebot.TeleBot(config.TOKEN)

def main():
    posts = getPosts()
    current_day = datetime.today().day
    for post in posts:
        dt = datetime.fromtimestamp(mktime(post.published_parsed))
        if current_day == dt.day:
            sendPost(post)
        time.sleep(15)

def sendPost(post):
    title = post.title
    link = post.link
    description = post.description.split('\n')[1]

    html_msg = f"<a href='{link}'>📃 </a>{title}\n\n{description}"

    button_link = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton("Подробнее", link)
    button_link.add(url_button)
    bot.send_message(config.CHANNELNAME, html_msg, parse_mode='html', reply_markup=button_link)

def getPosts():
    news_feed = feedparser.parse(config.HTMLUrlArticles)
    return news_feed.entries

main()
