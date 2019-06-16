+++
# Date this page was created.
date = "2018-05-14"

# Project title.
title = "Data analytics dashboard using Python Flask and JavaScript Highcharts"

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

### Organization pattern

```
app.py
static/
templates/
    graph.html
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
    timeInterval = 120
    data = pd.DataFrame()
    featureList = ['market-price', 
                   'trade-volume']
    for feature in featureList:
        url = "https://api.blockchain.info/charts/"+feature+"?timespan="+str(timeInterval)+"days&format=json"
        data[feature] = pd.DataFrame(json.loads(urllib.request.urlopen(url).read().decode('utf-8'))['values'])['y']
    result = data.to_dict(orient='records')
    seq = [[item['market-price'], item['trade-volume']] for item in result]
    return jsonify(seq)
 
@app.route("/graph")
def graph():
    return render_template('graph.html')
 
if __name__ == '__main__':
    app.run(debug=True, threaded=True, host='0.0.0.0')
```

### templates/graph.html

```
<!DOCTYPE HTML>
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
		<title>Highstock Example</title>
        <script src="{{ url_for('static', filename='jquery-1.8.3.min.js') }}"></script>
		<script type="text/javascript">
		$(function () {
            $.getJSON('http://localhost:5000/data.json', function (data) {
                Highcharts.stockChart('container', {
                    rangeSelector: {
                        selected: 1
                    },
                    title: {
                        text: 'AAPL Stock Price'
                    },
                    series: [{
                        name: 'AAPL',
                        data: data,
                        tooltip: {
                            valueDecimals:10
                        }
                    }]
                });
            });
        });
		</script>
	</head>
	<body>
        <script src="https://code.jquery.com/jquery-3.1.1.min.js"></script>
        <script src="https://code.highcharts.com/stock/highstock.js"></script>
        <script src="https://code.highcharts.com/stock/modules/exporting.js"></script>
        <script src="https://code.highcharts.com/stock/modules/export-data.js"></script>
        <div id="container" style="height: 400px; min-width: 310px"></div>
	</body>
</html>
```
