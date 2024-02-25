import logging
from flask import Flask,request
from telegram.ext import Updater,CommandHandler,MessageHandler,Filters,Dispatcher,Handler
from telegram import Bot,Update,ReplyKeyboardMarkup
from utils import get_reply,fetch_news,topic_keyboard
import os


link=os.environ['url_link']
Token=os.environ['token']
print(link)
# enable logging
# General Logging For Any Telegram Bot Program
logging.basicConfig(format='%(asctime)s - %(name)s -%(levelname)s -%(message)s',
                    level=logging.INFO)
logger=logging.getLogger(__name__)

app=Flask(__name__)

@app.route('/')
def index():
    return 'Telegram News Bot By Samarth'

@app.route(f'/{Token}',methods=['GET','POST'])
def webhook():
    '''WebHook which receives updates from telegram bot'''
    # create update object from json-format request data
    update=Update.de_json(request.get_json(),bot)
    # process update
    dp.process_update(update)
    return 'ok'

def start(bot,update):
    print(bot)
    author=bot.message.chat.first_name
    msg=bot.message.text
    print(msg)
    reply=f'Hi {author}'
    bot.message.reply_text(reply)

def _help(bot,update):
    help_text='Hey, What Help You Need'
    bot.message.reply_text(help_text)

def answer_text(bot,update):
    intent , reply=get_reply(bot.message.text,bot.message.chat_id)
    if intent=='get_news':
        articles=fetch_news(reply)
        for article in articles:
            bot.message.reply_text(article['link'])
    else:
        bot.message.reply_text(reply)

def echo_sticker(bot,update):
    print(bot.message.sticker.file_id)
    bot.message.reply_sticker(bot.message.sticker.file_id)

def news (bot,update):
    bot.message.reply_text(text='Choose a category',
                    reply_markup=ReplyKeyboardMarkup(keyboard=topic_keyboard,one_time_Keyboard=True))

    
def error(bot,update):
    logger.error(f'Update {update} caused error {update.error}')

# ports for webhooks 443,80,88,8443
    
# if __name__=='__main__':
    
bot=Bot(Token)
try:
    bot.set_webhook(f"{link}"+Token)
except Exception as e:
    print(e)
dp=Dispatcher(bot,None)
# updater=Updater(Token)
# dp=updater.dispatcher
print(dp)
dp.add_handler(CommandHandler('start',start))
dp.add_handler(CommandHandler('help',_help))
dp.add_handler(CommandHandler('news',news))
dp.add_handler(MessageHandler(Filters.text,answer_text))
dp.add_handler(MessageHandler(Filters.sticker,echo_sticker))
# dp.add_error_handler(error)
if __name__=='__main__':
    app.run(port=8440)
# logger.info('Started Pooling...')
# updater.start_polling() # start pooling
# updater.idle() # wait for user to stop program