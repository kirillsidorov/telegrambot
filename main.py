import telebot
import feedparser
import time
import config
import ssl
import requests

ssl._create_default_https_context = ssl._create_unverified_context
bot = telebot.TeleBot(config.TOKEN)


def post():
    news_feed = feedparser.parse(config.htmlurlarticles)
    for entry in news_feed.entries:
        title = entry.title
        link = entry.link
        description = entry.description.split('\n')[1]

        html_msg = "<a href='" + link + "'>" + "📃 " + "</a> " + \
                   title + "\n" + \
                   "\n" + \
                   description

        bot.send_message(config.channel, html_msg, parse_mode='html')

        time.sleep(int(15))


post()
