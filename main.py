from fastapi import FastAPI
import requests

app = FastAPI()

# MA'LUMOTLAR
GOOGLE_API_KEY = "AIzaSyCZTpdwJzQ8a85JGD491l1ygDZtNiD3ZhY"
# To'g'ridan-to'g'ri Google API havolasi
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GOOGLE_API_KEY}"

@app.get("/")
def home():
    return {"message": "Sems AI Server 2.0 ishlayapti!"}

@app.get("/ask")
def ask_ai(query: str):
    try:
        # Google API ga yuboriladigan ma'lumot (JSON formatida)
        payload = {
            "contents": [{
                "parts": [{"text": f"Sen aqlli yordamchi Semsan. Savolga juda qisqa javob ber. Savol: {query}"}]
            }]
        }
        
        # Zapros yuboramiz
        response = requests.post(API_URL, json=payload)
        res_json = response.json()
        
        # Javobni ichidan sug'urib olamiz
        if "candidates" in res_json:
            answer = res_json["candidates"][0]["content"]["parts"][0]["text"]
            return {"reply": answer}
        else:
            return {"reply": "Xatolik: Google javob bermadi. Kalitni tekshiring."}

    except Exception as e:
        return {"reply": f"Server xatosi: {str(e)}"}
