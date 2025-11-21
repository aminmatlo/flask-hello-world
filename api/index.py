from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/live", methods=["GET"])
def live_api():
    params = request.args.to_dict()
    url = "https://version.ffmax.purplevioleto.com/live/ver.php"

    headers = {
        'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 15; SM-A165F Build/AP3A.240905.015.A2)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "gzip",
        'X-Unity-Version': "2018.4.11f1"
    }

    try:
        r = requests.get(url, headers=headers, params=params, timeout=10)
        data = r.json()
        data["server_url"] = "https://loginbp.karim.com/"
        return jsonify(data)
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Request failed", "details": str(e)}), 500
    except ValueError:
        return jsonify({"error": "Response is not valid JSON"}), 500
