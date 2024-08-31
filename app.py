from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    # Here you would add logic to handle the registration process
    return jsonify({'response': 'Welcome to the Farmer Registration Bot!'})

if __name__ == '__main__':
    app.run(debug=True)
