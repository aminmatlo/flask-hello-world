from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/live/ver.php')
def live_ver():
    url = (
        "https://version.ffmax.purplevioleto.com/live/ver.php?"
        "version=2.117.9&lang=ar&device=android&channel=android_max&"
        "appstore=googleplay_max&region=ME&release_version=OB51&"
        "whitelist_version=1.4.0&whitelist_sp_version=1.0.0&"
        "device_name=samsung%20SM-A165F&device_CPU=ARM64%20FP%20ASIMD%20AES&"
        "device_GPU=Mali-G57%20MC2&device_mem=3621"
    )

    headers = {
        'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 15; SM-A165F Build/AP3A.240905.015.A2)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "gzip",
        'X-Unity-Version': "2018.4.11f1"
    }

    try:
        response = requests.get(url, headers=headers)
        return response.text
    except Exception as e:
        return jsonify({"error": str(e)}), 500
