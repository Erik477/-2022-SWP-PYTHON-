import json
from flask import Flask, jsonify



app = Flask(__name__)
@app.route('/statistic')
def statistic(): 
    with open('playerstats.json', 'r') as f:
        playerstats = json.load(f)

    return jsonify({"Player: ": playerstats})

app.run()