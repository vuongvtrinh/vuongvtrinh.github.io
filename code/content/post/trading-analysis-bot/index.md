+++
# Date this page was created.
date = "2018-01-01"

# Project title.
title = "A Telegram chatbot for data-driven analytics of crypto-market: on-chain versus off-chain transactions"

# Project summary to display on homepage.
summary = "A tutorial to develop a Telegram chatbot for data-driven analytics of cryptoassets from both utility and speculation perspectives."

# Optional image to display on homepage (relative to `static/img/` folder).
image_preview = "chatbot.jpg"

# Tags: can be used for filtering projects.
tags = ["blockchain-cryptoasset", "quantitative-analytics"]

# Optional external URL for project (replaces project detail page).
external_link = ""

# Does the project detail page use math formatting?
math = true

# Optional featured image (relative to `static/img/` folder).
[header]
image = ""
caption = ""

# Featured image
# To use, add an image named `featured.jpg/png` to your project's folder. 
[image]
  # Caption (optional)
  caption = ""

  # Focal point (optional)
  # Options: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight
  focal_point = ""

  # Show image only in page previews?
  preview_only = true

+++

## Introduction

A tutorial to develop a Telegram chatbot for data-driven analytics of cryptoassets from both utility and speculation perspectives.

- Telegram chatbot: [https://t.me/trading_analysis_bot](https://t.me/trading_analysis_bot)
- Github repository: [https://github.com/trinhvv/trading-analysis-bot](https://github.com/trinhvv/trading-analysis-bot)

## Technology

- Chatbot
- Financial time series data visualization and analysis
- Databases and access management
- Web scraping

## Requirements

```
python-telegram-bot
python-binance
numpy
datetime
matplotlib
seaborn
six
pandas
sqlalchemy
psycopg2
beautifulsoup4
requests
```

## Source code

```
import os
import telegram
from telegram import ParseMode
from telegram.ext import Updater, CommandHandler
from binance.client import Client
from binance_trading_bot import analysis, monitor, news, bitcoin, supply
from sqlalchemy import create_engine
from pandas.io import sql

MANUAL_TEXT = """Data-driven analytics of crypto-market on Binance.

*Asset info*
Syntax: /i <asset>
Usage: /i oax or /i algo bnb.
*Transaction analysis*
Syntax: /s <asset>
Usage: /s qtum or /s btt fet.
*Supply analysis*
Syntax: /x <asset> <time-frame> <n-day>
Usage: /x fet knc or /x dlt 4h 30. 
*Bitcoin aggregated charts*
Syntax: /b <n-day>
Usage: /b or /b 90.
*Market movement statistics*
Syntax: /m
Usage: /m.
Syntax: /e <n-day>
Usage: /e or /e 90.
*Newsflow*
Syntax: /n
Usage: /n.

Contact: @kakalotz
_Disclammer: only accessible for registered users._
 """

TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']
BINANCE_SECRET_KEY = os.environ['BINANCE_SECRET_KEY']
BINANCE_API_KEY = os.environ['BINANCE_API_KEY']
SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_DATABASE_URI']

engine = create_engine(SQLALCHEMY_DATABASE_URI)
conn = engine.raw_connection()
userList = sql.read_sql('SELECT * FROM "userList"', conn)
conn.close() 
userList = userList[userList['TRADING_ANALYSIS_BOT']==1]['USERNAME'].tolist()

client = Client(BINANCE_API_KEY, BINANCE_SECRET_KEY)

def x(bot, update, args):
    bot.send_chat_action(chat_id=update.message.chat_id, 
                         action=telegram.ChatAction.TYPING)
    if str(update.message.from_user.username) in userList:
        if args[-1].isdigit():
            TIME_FRAME_STEP_LIST = ['1h', '1h']
            TIME_FRAME_LIST = [args[-2]]
            TIME_FRAME_DURATION_LIST = [str(args[-1])+' days ago UTC']
            coinList = args[:-2]
        else:
            TIME_FRAME_STEP_LIST = ['1h', '1h']
            TIME_FRAME_LIST = ['4h', '1d']
            TIME_FRAME_DURATION_LIST = ['20 days ago UTC', '90 days ago UTC']
            coinList = args
        for coin in coinList:
            for i in range(len(TIME_FRAME_LIST)):
                TIME_FRAME_STEP = TIME_FRAME_STEP_LIST[i]
                TIME_FRAME = TIME_FRAME_LIST[i]
                TIME_FRAME_DURATION = TIME_FRAME_DURATION_LIST[i]
                try:
                    market = coin.upper()+'BTC'
                    supply.supply_analysis(client, market, TIME_FRAME_STEP, TIME_FRAME, TIME_FRAME_DURATION)
                    bot.send_photo(chat_id=update.message.chat_id, 
                               photo=open('img/'+market+'_'+TIME_FRAME.upper()+'.png', 'rb'))
                except Exception:
                    pass
                try:
                    market = coin.upper()+'USDT'
                    supply.supply_analysis(client, market, TIME_FRAME_STEP, TIME_FRAME, TIME_FRAME_DURATION)
                    bot.send_photo(chat_id=update.message.chat_id, 
                               photo=open('img/'+market+'_'+TIME_FRAME.upper()+'.png', 'rb'))
                except Exception:
                    pass
                    
def i(bot, update, args):
    bot.send_chat_action(chat_id=update.message.chat_id, 
                         action=telegram.ChatAction.TYPING)
    if str(update.message.from_user.username) in userList:
        for asset in args:
            asset = asset.upper()
            msg = analysis.asset_info(client, asset)
            update.message.reply_text(msg, parse_mode=ParseMode.MARKDOWN)

def s(bot, update, args):
    bot.send_chat_action(chat_id=update.message.chat_id, 
                         action=telegram.ChatAction.TYPING)
    if str(update.message.from_user.username) in userList:
        for asset in args:
            asset = asset.upper()
            msg = analysis.asset_analysis(client, asset)
            update.message.reply_text(msg, parse_mode=ParseMode.MARKDOWN)

def m(bot, update):
    bot.send_chat_action(chat_id=update.message.chat_id, 
                         action=telegram.ChatAction.TYPING)
    if str(update.message.from_user.username) in userList:
        msg = monitor.market_change(client)
        update.message.reply_text(msg, parse_mode=ParseMode.MARKDOWN)
        
def b(bot, update, args):
    bot.send_chat_action(chat_id=update.message.chat_id, 
                         action=telegram.ChatAction.TYPING)
    if str(update.message.from_user.username) in userList:
        try:
            timeInterval = int(args[0])
        except Exception:
            timeInterval = 120
        bitcoin.blockchain(timeInterval)
        bot.send_photo(chat_id=update.message.chat_id, 
                   photo=open('img/blockchain.png', 'rb'))
                   
def e(bot, update, args):
    bot.send_chat_action(chat_id=update.message.chat_id, 
                         action=telegram.ChatAction.TYPING)
    if str(update.message.from_user.username) in userList:
        try:
            timeInterval = int(args[0])
        except Exception:
            timeInterval = 120
        monitor.market_movement(client, timeInterval)
        bot.send_photo(chat_id=update.message.chat_id, 
                   photo=open('img/market.png', 'rb'))
        
def n(bot, update):
    bot.send_chat_action(chat_id=update.message.chat_id, 
                         action=telegram.ChatAction.TYPING)
    if str(update.message.from_user.username) in userList:
        msg = news.newsflow()
        update.message.reply_text(msg, 
                                  parse_mode=ParseMode.MARKDOWN,
                                  disable_web_page_preview=True)

def manual(bot,update):
    bot.send_message(chat_id=update.message.chat_id, 
                     text=MANUAL_TEXT, 
                     parse_mode=ParseMode.MARKDOWN, 
                     disable_web_page_preview=True)

def main():
    updater=Updater(TELEGRAM_TOKEN)
    dp=updater.dispatcher
    dp.add_handler(CommandHandler("start", manual))
    dp.add_handler(CommandHandler("help", manual))
    dp.add_handler(CommandHandler("m", m))
    dp.add_handler(CommandHandler("n", n))
    dp.add_handler(CommandHandler("i", i, pass_args=True))
    dp.add_handler(CommandHandler("b", b, pass_args=True))
    dp.add_handler(CommandHandler("e", e, pass_args=True))
    dp.add_handler(CommandHandler("x", x, pass_args=True))
    dp.add_handler(CommandHandler("s", s, pass_args=True))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
```

## Deployment on Heroku platform

### Initialize

```
heroku create trading-analysis-bot --buildpack heroku/python
```
### Setup Postgres database for user management

```
import pandas as pd
from sqlalchemy import create_engine
import json

with open('setting.txt') as json_file:  
    setting = json.load(json_file)

engine = create_engine(setting['SQLALCHEMY_DATABASE_URI'])
conn = engine.raw_connection()
customer = pd.read_csv("customer.csv")
customer.to_sql(name='userList', con=engine, if_exists='replace')
conn.close() 
```

### Deploy to the cloud

```
heroku config:set TELEGRAM_TOKEN=XXXXXXXXXXXXXXXXXXXXXXXXXX
heroku config:set BINANCE_SECRET_KEY=XXXXXXXXXXXXXXXXXXXXXXXXXX
heroku config:set BINANCE_API_KEY=XXXXXXXXXXXXXXXXXXXXXXXXXX
heroku config:set SQLALCHEMY_DATABASE_URI=XXXXXXXXXXXXXXXXXXXXXXXXXX
git push heroku master
heroku ps:scale bot=1 
```

## Snapshots

{{< gallery >}}

## License

MIT



