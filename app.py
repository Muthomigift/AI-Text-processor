from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import openai, os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
CORS(app)

client = openai.OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/process", methods=["POST"])
def process():
    try:
        text = request.json.get("text", "")
        if not text:
            return jsonify({"error": "No text provided"}), 400
        response = client.chat.completions.create(
            model="gemini-3.8-flash",
            messages=[{"role": "user", "content": text}]
        )
        return jsonify({"result": response.choices[0].message.content})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=PORT)