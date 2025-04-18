from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "MTN MoMo Server is Running"

@app.route('/pay', methods=['POST'])
def pay():
    data = request.json
    phone_number = data.get('phone_number')
    amount = data.get('amount')

    return jsonify({
        "status": "success",
        "message": f"Payment of {amount} requested for {phone_number}"
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
