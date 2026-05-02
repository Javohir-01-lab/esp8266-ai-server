from fastapi import FastAPI
import requests

app = FastAPI()

# GROQ API KALITINI SHU YERGA QO'YING
GROQ_API_KEY = "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"

@app.get("/")
def home():
    return "Sem AI Server ishlamoqda!"

@app.get("/ask")
def ask_ai(query: str):
    try:
        url = "https://api.groq.com/openai/v1/chat/completions"
        
        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": "llama-3.1-8b-instant",
            "messages": [
                {
                    "role": "system", 
                    "content": "Sening isming Sem. Sen aqlli muhandis yordamchisan. Har doim o'zbek tilida juda qisqa, bir jumlada javob ber."
                },
                {"role": "user", "content": query}
            ]
        }
        
        response = requests.post(url, json=payload, headers=headers)
        res_json = response.json()
        
        if "choices" in res_json:
            # FAQAT MATNNI QAYTARAMIZ (ESP8266 oson o'qishi uchun)
            answer = res_json["choices"][0]["message"]["content"]
            return answer
        else:
            return "Xato: API javob bermadi."

    except Exception as e:
        return f"Serverda xato: {str(e)}"
