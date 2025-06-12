from flask import Flask, request, jsonify
from mcr_romanization import romanize

app = Flask(__name__)

@app.route('/')
def index():
    return "McCune–Reischauer API is running!"

@app.route('/romanize', methods=['POST'])
def convert():
    data = request.get_json()
    text = data.get("text", "")
    result = romanize(text)
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
