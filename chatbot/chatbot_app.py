from flask import Flask, request, render_template
from ollama import Client

app = Flask(__name__)
ollama_client = Client(host="http://localhost:11434")

@app.route("/", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        user_message = request.form.get("message")
        if user_message:
            try:
                response = ollama_client.chat(
                    model="llama3.1",
                    messages=[{"role": "user", "content": user_message}]
                )
                bot_response = response["message"]["content"]
                return render_template("chat.html", user_message=user_message, bot_response=bot_response)
            except Exception as e:
                return render_template("chat.html", error=str(e))
    return render_template("chat.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)