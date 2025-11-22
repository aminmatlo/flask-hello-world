from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/live/ver.php')
def live_ver():
    params = request.args.to_dict()
    url = "https://version.ffmax.purplevioleto.com/live/ver.php"
    headers = {
        'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 15; SM-A165F Build/AP3A.240905.015.A2)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "gzip",
        'X-Unity-Version': "2018.4.11f1"
    }
    try:
        response = requests.get(url, headers=headers, params=params)
        return response.text
    except Exception as e:
        return jsonify({"error": str(e)}), 500
