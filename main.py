from fastapi import FastAPI
import requests

app = FastAPI()

# YANGI OLINGAN API KALIT
API_KEY = "AIzaSyBlV-VD-2jh-iieThXIItIfeusP0rZpoxs"

@app.get("/")
def home():
    return {"message": "Sems AI Server ishlamoqda!"}

@app.get("/ask")
def ask_ai(query: str):
    try:
        # DIQQAT: v1 versiyasi va aniq model nomi
        url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={API_KEY}"
        
        payload = {
            "contents": [{
                "parts": [{"text": f"Sen aqlli yordamchi Semsan. Qisqa javob ber: {query}"}]
            }]
        }
        
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, json=payload, headers=headers)
        res_json = response.json()
        
        # Agar xatolik bo'lsa, xatoni o'zini qaytaramiz
        if "error" in res_json:
            return {"reply": f"Xato: {res_json['error']['message']}"}

        # Javobni qaytarish
        if "candidates" in res_json:
            answer = res_json["candidates"][0]["content"]["parts"][0]["text"]
            return {"reply": answer}
        else:
            return {"reply": "Google javob qaytarmadi."}

    except Exception as e:
        return {"reply": f"Texnik xato: {str(e)}"}
