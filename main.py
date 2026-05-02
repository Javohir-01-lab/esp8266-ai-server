from fastapi import FastAPI
import requests

app = FastAPI()

# API kalitini o'rnating
GOOGLE_API_KEY = "AIzaSyBlV-VD-2jh-iieThXIItIfeusP0rZpoxs"

@app.get("/")
def home():
    return {"message": "Sems AI Server 5.0 ishlayapti!"}

@app.get("/ask")
def ask_ai(query: str):
    try:
        # Gemini 1.0 Pro modeliga murojaat qilamiz (eng barqaror variant)
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={GOOGLE_API_KEY}"
        
        payload = {
            "contents": [{
                "parts": [{"text": f"Sening isming Sem. Sen aqlli yordamchisans. Savolga juda qisqa javob ber. Savol: {query}"}]
            }]
        }
        
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, json=payload, headers=headers)
        res_json = response.json()
        
        if "error" in res_json:
            # Agar gemini-pro ham ishlamasa, oxirgi chora sifatida gemini-1.0-pro ni sinaymiz
            return {"reply": f"Google API Xatosi: {res_json['error']['message']}"}

        if "candidates" in res_json:
            answer = res_json["candidates"][0]["content"]["parts"][0]["text"]
            return {"reply": answer}
        else:
            return {"reply": "Google javob qaytarmadi."}

    except Exception as e:
        return {"reply": f"Serverda texnik xato: {str(e)}"}
