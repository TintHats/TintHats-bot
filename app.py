from flask import Flask, request, jsonify
from groq import Groq
import os

app = Flask(__name__)
cliente = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def obtener_respuesta(mensaje):
    historial = [
        {
            "role": "system",
            "content": (
                "Eres un vendedor casual y directo de TINT HATS, una tienda de gorras en Mexicali. "
                "Habla como una persona normal, sin formalismos. Respuestas cortas y al punto. "
                "Gorras G5 a $700, mayoreo de 3+ a $450. "
                "Gorras tela sencilla a $450, mayoreo de 3+ a $300. "
                "Envio gratis en Mexicali, zonas lejanas costo segun distancia. "
                "Cuando el cliente quiera comprar dile que te contacte por WhatsApp: 6865864989"
            )
        },
        {"role": "user", "content": mensaje}
    ]
    respuesta = cliente.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=historial
    )
    return respuesta.choices[0].message.content

@app.route("/", methods=["GET"])
def home():
    return "TINT HATS Chatbot corriendo!"

@app.route("/webhook", methods=["GET"])
def verificar():
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")
    if token == "tinthats2024":
        return challenge
    return "Token invalido", 403

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    try:
        mensaje = data["entry"][0]["messaging"][0]["message"]["text"]
        respuesta = obtener_respuesta(mensaje)
        print(f"Mensaje: {mensaje} | Respuesta: {respuesta}")
    except Exception as e:
        print(f"Error: {e}")
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
