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
        r = requests.get(url, headers=headers, params=params)
        data = r.json()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
