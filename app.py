from flask import Flask, request, jsonify, render_template
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Store chat history
chat_history = []

# 🖥️ Dashboard Page
@app.route("/")
def dashboard():
    return render_template("dashboard.html")

# 💬 Chatbot Page
@app.route("/chatbot")
def chatbot():
    return render_template("chat.html")

# 🤖 Chat API
@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_input = request.json.get("message", "")
        print("👤 User:", user_input)

        # Save history
        chat_history.append({"role": "user", "content": user_input})

        # Keep last 6 messages
        recent_history = chat_history[-6:]

        # System prompt
        system_prompt = """
        You are DataPro AI, a SaaS Customer Support Assistant.

        Your job:
        - Help users with login, password reset
        - Help with subscriptions, billing, pricing
        - Solve dashboard issues
        - Answer short, clear, and helpful
        - Be friendly and professional
        - If unsure, suggest contacting support

        Example:
        "Sure! Here's how you can reset your password..."
        """

        messages = [{"role": "system", "content": system_prompt}] + recent_history

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=messages
        )

        reply = response.choices[0].message.content

        # Save bot reply
        chat_history.append({"role": "assistant", "content": reply})

        print("🤖 Bot:", reply)

        return jsonify({"reply": reply})

    except Exception as e:
        print("🔥 ERROR:", str(e))
        return jsonify({"reply": "⚠️ Something went wrong. Please try again."})



if __name__ == "__main__":
    app.run(debug=False)
