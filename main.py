from fastapi import FastAPI
import requests

app = FastAPI()

# API kalitini o'rnating
GOOGLE_API_KEY = "AIzaSyBlV-VD-2jh-iieThXIItIfeusP0rZpoxs"

@app.get("/")
def home():
    return {"message": "Sems AI Server 4.0 ishlayapti!"}

@app.get("/ask")
def ask_ai(query: str):
    try:
        # API yo'li (Model nomi models/ prefiksi bilan va v1beta versiyasi)
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GOOGLE_API_KEY}"
        
        payload = {
            "contents": [{
                "parts": [{"text": f"Sening isming Sem. Sen aqlli yordamchisans. Savolga juda qisqa javob ber. Savol: {query}"}]
            }]
        }
        
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, json=payload, headers=headers)
        res_json = response.json()
        
        # Xatolikni tekshirish
        if "error" in res_json:
            return {"reply": f"Google API Xatosi: {res_json['error']['message']}"}

        if "candidates" in res_json:
            answer = res_json["candidates"][0]["content"]["parts"][0]["text"]
            return {"reply": answer}
        else:
            return {"reply": "Google javob qaytarmadi, xato format."}

    except Exception as e:
        return {"reply": f"Serverda texnik xato: {str(e)}"}
