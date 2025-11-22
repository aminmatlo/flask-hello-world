from flask import Flask, request
import requests
import re

app = Flask(__name__)

@app.route('/live/ver.php')
def live_ver():
    params = request.args.to_dict()
    user_agent = request.headers.get('User-Agent', 'Dalvik/2.1.0 (Linux; U; Android 15; SM-A165F Build/AP3A.240905.015.A2)')
    url = "https://version.ffmax.purplevioleto.com/live/ver.php"
    headers = {
        'User-Agent': user_agent,
        'Connection': "Keep-Alive",
        'Accept-Encoding': "gzip",
        'X-Unity-Version': "2018.4.11f1"
    }
    try:
        response = requests.get(url, headers=headers, params=params, timeout=5)
        text = response.text
        text = re.sub(
            r'("server_url"\s*:\s*")[^"]+(")',
            r'\1https://versionffmaxpurplevioleto.vercel.app/\2',
            text
        )
        return "si"
    except Exception as e:
        return f'{{"error":"{str(e)}"}}', 500
