import telebot
import feedparser
import time
import config
import ssl
import requests
from telebot import types

ssl._create_default_https_context = ssl._create_unverified_context
bot = telebot.TeleBot(config.TOKEN)

def main():
    posts = getPosts()
    for post in posts:
        sendPost(post)
        time.sleep(15)

def sendPost(post):
    title = post.title
    link = post.link
    description = post.description.split('\n')[1]

    html_msg = "<a href='" + link + "'>" + "📃 " + "</a> " + \
               title + "\n" + \
               "\n" + \
               description

    button_link = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton("Подробнее", link)
    button_link.add(url_button)
    bot.send_message(config.channel, html_msg, parse_mode='html', reply_markup=button_link)


def getPosts():
    news_feed = feedparser.parse(config.htmlurlarticles)
    return news_feed.entries


main()
