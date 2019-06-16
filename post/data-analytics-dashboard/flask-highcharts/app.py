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