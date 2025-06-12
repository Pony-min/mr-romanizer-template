from flask import Flask, request, jsonify
from mcr_romanization import romanize

app = Flask(__name__)

@app.route('/')
def index():
    return "McCune–Reischauer API is running!"

@app.route('/romanize', methods=['POST'])
def convert():
    try:
        data = request.get_json()
        print("📩 Received payload:", data)

        text = data.get("text", "")
        print("🔍 Input text:", text)

        result = romanize(text)
        print("✅ Romanized result:", result)

        return jsonify({"result": result})
    
    except Exception as e:
        import traceback
        print("❌ Exception occurred:", e)
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
