from fastapi import FastAPI
import requests

app = FastAPI()

# API kalitini o'rnating
API_KEY = "AIzaSyBlV-VD-2jh-iieThXIItIfeusP0rZpoxs"

@app.get("/")
def home():
    return {"message": "Sems Server 7.0 ishlamoqda!"}

@app.get("/ask")
def ask_ai(query: str):
    try:
        # Eng barqaror va hamma joyda ishlaydigan endpoint (v1beta)
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"
        
        payload = {
            "contents": [{
                "parts": [{"text": f"Sen Semsan. Juda qisqa javob ber: {query}"}]
            }]
        }
        
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, json=payload, headers=headers)
        res_json = response.json()
        
        # Xatolikni aniqlash
        if "error" in res_json:
            # Agar gemini-1.5-flash topilmasa, gemini-pro ni sinab ko'ramiz
            fallback_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={API_KEY}"
            response = requests.post(fallback_url, json=payload, headers=headers)
            res_json = response.json()

        if "candidates" in res_json:
            answer = res_json["candidates"][0]["content"]["parts"][0]["text"]
            return {"reply": answer}
        else:
            return {"reply": "Google hozircha band, birozdan so'ng urinib ko'ring."}

    except Exception as e:
        return {"reply": f"Texnik xato: {str(e)}"}
