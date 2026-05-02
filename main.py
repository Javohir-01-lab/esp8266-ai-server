from fastapi import FastAPI
import requests

app = FastAPI()

# YANGI OLINGAN API KALITNI SHU YERGA QO'YING
API_KEY = "AIzaSyBlV-VD-2jh-iieThXIItIfeusP0rZpoxs"

@app.get("/")
def home():
    return {"message": "Server tayyor!"}

@app.get("/ask")
def ask_ai(query: str):
    try:
        # Eng oddiy va hamma joyda ishlaydigan endpoint
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"
        
        payload = {
            "contents": [{"parts": [{"text": query}]}]
        }
        
        response = requests.post(url, json=payload)
        res_json = response.json()
        
        # Agar xato bo'lsa, xatoni o'zini ko'rsatadi
        if "error" in res_json:
            return {"reply": "Google xatosi: " + res_json["error"]["message"]}
            
        return {"reply": res_json["candidates"][0]["content"]["parts"][0]["text"]}
    except Exception as e:
        return {"reply": "Tizim xatosi: " + str(e)}
