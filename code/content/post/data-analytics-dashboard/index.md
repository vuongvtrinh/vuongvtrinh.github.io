+++
# Date this page was created.
date = "2018-05-14"

# Project title.
title = "Data Analytics Dashboard using Python Flask and JavaScript Highcharts"

# Project summary to display on homepage.
summary = "A tutorial to develop a web dashboard for data analytics using Python Flask and JavaScript Highcharts."

# Optional image to display on homepage (relative to `static/img/` folder).
image_preview = ""

# Tags: can be used for filtering projects.
tags = ["data-science", "flask", "highcharts"]

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

A tutorial to develop a web dashboard for data analytics using Python Flask and JavaScript Highcharts.

- GitHub repository: [https://github.com/trinhvv/flask-highcharts](https://github.com/trinhvv/flask-highcharts)
- Live demo: [https://flask-highcharts.herokuapp.com](https://flask-highcharts.herokuapp.com)

## Tutorial

- Fetch data from [https://www.blockchain.com/](https://www.blockchain.com/)
- Data preprocessing in Flask then parse to Highcharts
- Deploy to Heroku

### Structure

```
app.py
Procfile
requirements.txt
runtime.txt
static/
templates/
    index.html
```

### requirements.txt

```
Flask
gunicorn
pandas
six
```

### app.py

```
from flask import Flask, render_template, jsonify
import pandas as pd
from six.moves import urllib
import json
 
app = Flask(__name__)
 
@app.route("/data.json")
def data():
    timeInterval = 1000
    data = pd.DataFrame()
    featureList = ['market-price', 
                   'trade-volume']
    for feature in featureList:
        url = "https://api.blockchain.info/charts/"+feature+"?timespan="+str(timeInterval)+"days&format=json"
        data['time'] = pd.DataFrame(json.loads(urllib.request.urlopen(url).read().decode('utf-8'))['values'])['x']*1000
        data[feature] = pd.DataFrame(json.loads(urllib.request.urlopen(url).read().decode('utf-8'))['values'])['y']
    result = data.to_dict(orient='records')
    seq = [[item['time'], item['market-price'], item['trade-volume']] for item in result]
    return jsonify(seq)
 
@app.route("/")
def index():
    return render_template('index.html')
 
if __name__ == '__main__':
    app.run(debug=True, threaded=True, host='0.0.0.0')
```

### templates/index.html

```
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
  <head>
    <title>
      Chart
    </title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <script src="https://code.jquery.com/jquery-3.1.1.min.js"></script>
    <script src="https://code.highcharts.com/stock/highstock.js"></script>
    <script src="https://code.highcharts.com/stock/modules/exporting.js"></script>
    <script type="text/javascript">
        $.getJSON('/data.json', function (data) {
            // create the chart
            Highcharts.stockChart('container', {
                title: {
                    text: 'Bitcoin'
                },
                rangeSelector: {
                    selected: 1,
                    inputEnabled: false
                },
                series: [{
                    name: 'Bitcoin',
                    data: data,
                    tooltip: {
                        valueDecimals: 2
                    }
                }]
            });
        });
    </script>
  </head>
  <body>
    <div id="container" style="height: 400px; min-width: 310px; max-width: 1000px"></div>
  </body>
</html>
```

### Procfile

```
web: gunicorn app:app --log-file=-
```

### runtime.txt

```
python-3.6.5
```

## Deploy to Heroku

```
heroku create flask-highcharts --buildpack heroku/python
heroku login
git init
heroku git:remote -a flask-highcharts
git add .
git commit -am "make it better"
git push heroku master
heroku ps:scale bot=1 
```

## Screenshot

![screenshot.png](screenshot.png)

