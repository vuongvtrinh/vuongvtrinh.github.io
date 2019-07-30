+++
# Date this page was created.
date = "2018-01-01"

# Project title.
title = "Quantitative Analytics and Trading Strategies"

# Project summary to display on homepage.
summary = "This project develops an intelligent data driven application to monitor blockchain projects and to analyze cryptoassets from both utility and speculation perspectives."

# Optional image to display on homepage (relative to `static/img/` folder).
image_preview = ""

# Tags: can be used for filtering projects.
tags = ["blockchain-cryptoasset", "quantitative-analytics"]

# Optional external URL for project (replaces project detail page).
external_link = ""

# Does the project detail page use math formatting?
math = false

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

This project develops an intelligent data driven application to monitor blockchain projects and to analyze cryptoassets from both utility and speculation perspectives. We target blockchain entrepreneurs, investors and traders all along the life of projects: token generation, listing on secondary market, product delivery, product usage, and token valorization.

## Data-Driven Financial Analytics

### Fundamental information

```
#EVX
Type: TOKEN
Website: https://www.everex.io/
Social Media: 
- https://t.me/everexio
- https://www.facebook.com/everex.io
- https://twitter.com/everexio
Explorers: 
- https://etherscan.io/token/0xf3db5fa2c66b7af3eb0c0b782510816cbe4813b8
Source Code: https://github.com/EverexIO/Et
Market Cap: $12,407,222
Current Price: $0.548992
Issue Price: $0.880000
Issue Date: 2017-10-11
Max Supply: -
Total Supply: 25,000,000
Circulating Supply: 22,600,000
```

### Transaction analysis

```
#TNTBTC 92,966,054.00 (94.84%)
P: 0.00000730 V: 608.23 VWAP: 0.00000654
30 mins: Buy 12.07 Sell 6.42
15 mins: Buy 8.37 Sell 3.97
5 mins: Buy 4.19 Sell 2.16
#TNTETH 5,059,783.00 (5.16%)
P: 0.00026182 V: 1,194.92 VWAP: 0.00023616
30 mins: Buy 13.32 Sell 12.58
15 mins: Buy 8.04 Sell 2.38
5 mins: Buy 1.76 Sell 1.99
```

### Supply and demand analysis

![x.png](x.png)

### Market movement statistics

```
#MARKET
USDⓈ: 20 (+) 113 (-)
ALTS: 43 (+) 89 (-)
BNB: 63 (+) 30 (-)
BTC: 120 (+) 31 (-)
Tue Jul  2 13:48:21 2019
```

### Market moneyflow analysis

![binance.png](binance.png)

### Bitcoin aggregated charts

![blockchain.png](blockchain.png)

### Newsflow sentiment analysis

![n.png](n.png)

## Basic Trading Strategies

### Ping/Pong Order

Ping/pong submits multiple 'ping' orders; once a ping order fills, an associated 'pong' order is submitted.

Multiple ping/pong pairs can be created by specifying an order count greater than 1, a suitable min/max ping price, and a pong distance. Multiple ping orders will be created between the specified min/max prices, with the associated pongs offset by the pong distance from the ping price.

### Iceberg Order
Iceberg allows you to place a large order on the market while ensuring only a small part of it is ever filled at once. 

### TWAP Order

TWAP spreads an order out through time in order to fill at the time-weighted average price, calculated between the time the order is submitted to the final atomic order close.

The price can be specified as a fixed external target, such as the top bid/ask or last trade price, or as an explicit target which must be matched against the top bid/ask/last trade/etc.

### Accumulate/Distribute Order

Accumulate/Distribute allows you to break up a large order into smaller randomized chunks, submitted at regular or irregular intervals to minimise detection by other players in the market.

## Advanced Trading Strategies

### Statistical arbitrage via pairs trading

### Trailing stop and short sell via iceberge order

### Pure market maker

### Portfolio management and optimization

## Screenshots

{{< gallery >}}

