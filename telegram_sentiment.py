# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 00:40:27 2020

@author: ACER
"""

import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from prediction import predict

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
logger = logging.getLogger(__name__)

def start(update,context):
    update.message.reply_text("Lets begin the word war shall we?")
    
def pred(update,context):
    update.message.reply_text(predict(update.message.text))
    
def error(update,context):
    logger.warning('Update "%s" caused "%s" error',update,context.error)
    
def main():
    updater = Updater("1002731806:AAF2Il5Q-h7IHwtHcXNv76ahBIN_c17pM0g", use_context = True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start",start))
    dp.add_handler(MessageHandler(Filters.text,pred))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
    