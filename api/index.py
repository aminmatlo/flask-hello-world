from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/live/', methods=['GET'])
def live():
    # أخذ جميع الـ query parameters وتحويلها إلى dict
    params = request.args.to_dict()
    
    # إرجاعهم على شكل JSON
    return jsonify(params)
