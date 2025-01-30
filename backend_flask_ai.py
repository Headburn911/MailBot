import openai
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

client = openai.OpenAI(api_key="JOUW_OPENAI_API_KEY")

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

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Je bent een AI-assistent die helpt bij het schrijven van professionele e-mails."},
            {"role": "user", "content": prompt}
        ]
    )

    email_text = response.choices[0].message.content
    return jsonify({"email": email_text})  # LET OP: correcte inspringing!

if __name__ == "__main__":
    app.run(debug=True, port=5000)
