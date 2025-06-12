from flask import Flask, request, jsonify

app = Flask(__name__)

def romanize(text):
    return "mr-" + text

@app.route('/')
def index():
    return "MR Romanizer API is running!"

@app.route('/romanize', methods=['POST'])
def convert():
    data = request.get_json()
    text = data.get("text", "")
    return jsonify({"result": romanize(text)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
