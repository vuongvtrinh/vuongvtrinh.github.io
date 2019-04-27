+++
# Date this page was created.
date = "2018-01-01"

# Project title.
title = "A Telegram chatbot for data-driven analytics of crypto-market on Binance: on-chain vs. off-chain transactions"

# Project summary to display on homepage.
summary = "How to invent a Telegram chatbot for data-driven analytics of crypto-assets from both utility and speculation perspectives."

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

## Source code

```
import os
import telegram
from telegram import ParseMode
from telegram.ext import Updater, CommandHandler
from binance.client import Client
from binance_trading_bot import analysis, monitor, news, bitcoin, supply, volume
from sqlalchemy import create_engine
from pandas.io import sql

MANUAL_TEXT = """Data-driven analytics of crypto-market on Binance.
*Features*
- Altcoin supply analysis
- Exchange movement statistics
- Bitcoin aggregated charts
- Newsflow
*Commands*
- /x <coin>
Usage: /x fet knc. 
- /t <market>
Usage: /t qtumusdt or /t btt xlmusdt bttbnb.
- /s <asset>
Usage: /s qtum or /s btt fet.
- /m
Usage: /m.
- /b <n-day>
Usage: /b or /b 90.
- /e <n-day>
Usage: /e or /e 90.
- /n
Usage: /n.
*Supports*
Start trading on [Binance](https://www.binance.com/?ref=13339920), [Huobi](https://www.huobi.br.com/en-us/topic/invited/?invite_code=x93k3) or [Coinbase](https://www.coinbase.com/join/581a706d01bc8b00dd1d1737).
Use the [Brave](https://brave.com/ken335) privacy browser to earn BAT token.
BTC tipjar: [1DrEMhMP5rAytKyKXRzc6szTcUX8bZzZgq](1DrEMhMP5rAytKyKXRzc6szTcUX8bZzZgq).
*Contact*
@kakalotz
_Disclammer: only accessible for registered users._
 """

TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']
BINANCE_SECRET_KEY = os.environ['BINANCE_SECRET_KEY']
BINANCE_API_KEY = os.environ['BINANCE_API_KEY']
SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_DATABASE_URI']

engine = create_engine(SQLALCHEMY_DATABASE_URI)
conn = engine.raw_connection()
userList = sql.read_sql('SELECT * FROM "userList"', conn)['USERNAME'].tolist()
conn.close() 

client = Client(BINANCE_API_KEY, BINANCE_SECRET_KEY)

def x(bot, update, args):
    bot.send_chat_action(chat_id=update.message.chat_id, 
                         action=telegram.ChatAction.TYPING)
    if str(update.message.from_user.username) in userList:
        TIME_FRAME_STEP = '4h'
        TIME_FRAME_LIST = ['4h', '1d']
        TIME_FRAME_DURATION_LIST = ['45 days ago UTC', '90 days ago UTC']
        for coin in args:
            market = coin.upper()+'BTC'
            for i in range(len(TIME_FRAME_LIST)):
                TIME_FRAME = TIME_FRAME_LIST[i]
                TIME_FRAME_DURATION = TIME_FRAME_DURATION_LIST[i]
                try:
                    supply.supply_analysis(client, market, TIME_FRAME_STEP, TIME_FRAME, TIME_FRAME_DURATION)
                    bot.send_photo(chat_id=update.message.chat_id, 
                               photo=open('img/'+market+'_'+TIME_FRAME.upper()+'.png', 'rb'))
                except Exception:
                    pass

def t(bot, update, args):
    bot.send_chat_action(chat_id=update.message.chat_id, 
                         action=telegram.ChatAction.TYPING)
    if str(update.message.from_user.username) in userList:
        for market in args:
            market = market.upper()
            TIME_FRAME_STEP = ['1d', '1d', '4h']
            TIME_FRAME = ['1w', '1d', '4h']
            TIME_FRAME_DURATION = ['365 days ago UTC', '90 days ago UTC', '14 days ago UTC']
            try:
                volume.analysis_visual(client, market, TIME_FRAME_STEP, TIME_FRAME, TIME_FRAME_DURATION)
            except Exception:
                market = market+'BTC'
                volume.analysis_visual(client, market, TIME_FRAME_STEP, TIME_FRAME, TIME_FRAME_DURATION)
            bot.send_photo(chat_id=update.message.chat_id, 
                       photo=open('img/'+market+'.png', 'rb'))

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
        bitcoin.bid_ask_sum()
        bot.send_photo(chat_id=update.message.chat_id, 
                   photo=open('img/bidasksum.png', 'rb'))
        monitor.market_movement(client, timeInterval)
        bot.send_photo(chat_id=update.message.chat_id, 
                   photo=open('img/market.png', 'rb'))
                   
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
    dp.add_handler(CommandHandler("b", b, pass_args=True))
    dp.add_handler(CommandHandler("e", e, pass_args=True))
    dp.add_handler(CommandHandler("x", x, pass_args=True))
    dp.add_handler(CommandHandler("t", t, pass_args=True))
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

### Deploy to the cloud

```
heroku create trading-analysis-bot --buildpack heroku/python
heroku config:set TELEGRAM_TOKEN=XXXXXXXXXXXXXXXXXXXXXXXXX
heroku config:set BINANCE_SECRET_KEY=XXXXXXXXXXXXXXXXXXXXXXXXX
heroku config:set BINANCE_API_KEY=XXXXXXXXXXXXXXXXXXXXXXXXX
heroku config:set SQLALCHEMY_DATABASE_URI=XXXXXXXXXXXXXXXXXXXXXXXXX
git push heroku master
heroku ps:scale bot=1 
```

## Snapshots

{{< gallery >}}

## License

MIT



