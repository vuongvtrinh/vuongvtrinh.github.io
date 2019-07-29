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
Market Cap: $18,108,409
Current Price: $0.801257
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
Iceberg allows you to place a large order on the market while ensuring only a small part of it is ever filled at once. By enabling the 'Excess As Hidden' option, it is possible to offer up the remainder as a hidden order, allowing for minimal market disruption when executing large trades.

### TWAP Order

TWAP spreads an order out through time in order to fill at the time-weighted average price, calculated between the time the order is submitted to the final atomic order close.

The price can be specified as a fixed external target, such as the top bid/ask or last trade price, or as an explicit target which must be matched against the top bid/ask/last trade/etc.

Available price targets/explicit target conditions:
* OB side price (top bid/ask)
* OB mid price
* Last trade price

### Accumulate/Distribute Order

Accumulate/Distribute allows you to break up a large order into smaller randomized chunks, submitted at regular or irregular intervals to minimise detection by other players in the market.

By enabling the 'Await Fill' option, the algorithm will ensure each component fills before submitting subsequent orders. Enabling the 'Catch Up' flag will cause the algorithm to ignore the slice interval for the next order if previous orders have taken longer than expected to fill, thereby ensuring the time-to-fill for the entire order is not adversely affected.

The price must be manually specified as `limitPrice` for `LIMIT` order types, or as a combination of a price offset & cap for `RELATIVE` order types. `MARKET` A/D orders execute using `MARKET` atomic orders, and offer no price control.

For `RELATIVE` A/D orders, the price offset & cap can both be set to one of the following:
* Top ask
* Top bid
* Orderbook mid price
* Last trade price
* Moving Average (configurable period, time frame, candle price)
* Exponential Moving Average (configurable period, time frame, candle price)

## Advanced Trading Strategies

### Statistical arbitrage via pairs trading

### Trailing stop and short sell via iceberge order

### Pure market maker

### Portfolio management and optimization

## Screenshots

{{< gallery >}}

