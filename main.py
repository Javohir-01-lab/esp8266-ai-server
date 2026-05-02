
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

from fastapi import FastAPI
import requests

app = FastAPI()

# GROQ API KALITINI SHU YERGA QO'YING
GROQ_API_KEY = "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"

@app.get("/")
def home():
    return {"message": "Sems AI 2026 (Llama 3.1) ishlamoqda!"}

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
            "content": "Sening isming Sem. Sen aqlli va ko'p qirali mutaxasis yordamchisan. Har doim o'zbek tilida juda qisqa, aniq va london javob ber!."
        },
        {"role": "user", "content": query}
    ]
} 
        
        response = requests.post(url, json=payload, headers=headers)
        res_json = response.json()
        
        if "choices" in res_json:
            answer = res_json["choices"][0]["message"]["content"]
            return {"reply": answer}
        else:
            return {"reply": f"Groq API xatosi: {str(res_json)}"}

    except Exception as e:
        return {"reply": f"Serverda texnik xato: {str(e)}"}
