from groq import Groq
import os

# 🔑 Replace with your Groq API key
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

try:
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": "Say hello in one line"}
        ]
    )

    print("✅ API is working!")
    print("🤖 Response:", response.choices[0].message.content)

except Exception as e:
    print("❌ API not working")
    print("Error:", str(e))