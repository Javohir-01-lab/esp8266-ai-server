from fastapi import FastAPI
import requests

app = FastAPI()

# GROQ API KALITINI SHU YERGA QO'YING
GROQ_API_KEY = "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"

@app.get("/")
def home():
    return {"message": "Sems AI (Groq) ishlamoqda!"}

@app.get("/ask")
def ask_ai(query: str):
    try:
        url = "https://api.groq.com/openai/v1/chat/completions"
        
        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": "llama3-8b-8192",
            "messages": [
                {"role": "system", "content": "Sen Semsan, aqlli yordamchi muhandissan. Juda qisqa va aniq javob ber."},
                {"role": "user", "content": query}
            ]
        }
        
        response = requests.post(url, json=payload, headers=headers)
        res_json = response.json()
        
        if "choices" in res_json:
            answer = res_json["choices"][0]["message"]["content"]
            return {"reply": answer}
        else:
            return {"reply": f"Xato: {str(res_json)}"}

    except Exception as e:
        return {"reply": f"Serverda xato: {str(e)}"}
