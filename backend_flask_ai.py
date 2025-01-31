import google.generativeai as genai
import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Gebruik de API-key als omgevingsvariabele
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Stel de API-key in voor Google Gemini
genai.configure(api_key=GEMINI_API_KEY)

@app.route("/generate-email", methods=["POST"])
def generate_email():
    data = request.json
    subject = data.get("subject", "")
    tone = data.get("tone", "")
    recipient = data.get("recipient", "")

    prompt = f"""
    Schrijf een professionele e-mail met het volgende onderwerp: "{subject}".
    De toon moet {tone} zijn en de e-mail is bedoeld voor {recipient}.
    """

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)

    return jsonify({"email": response.text})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
