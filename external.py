from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/tax')
def tax():
    return jsonify(Tax=15), 200

if __name__ == "__main__":
    app.run(debug=True, port=5000)