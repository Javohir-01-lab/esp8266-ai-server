from fastapi import FastAPI
import google.generativeai as genai
import os

app = FastAPI()

# API kalitini o'rnatish
GOOGLE_API_KEY = "AIzaSyCZTpdwJzQ8a85JGD491l1ygDZtNiD3ZhY"
genai.configure(api_key=GOOGLE_API_KEY)

# Modelni tanlash (To'g'ri yozilgan varianti)
model = genai.GenerativeModel('gemini-1.5-flash-latest')

@app.get("/")
def home():
    return {"message": "Server ishlayapti!"}

@app.get("/ask")
def ask_ai(query: str):
    try:
        # Tizimga Sem (JARVIS uslubida) xarakterini beramiz
        instruction = "Sen aqlli yordamchi Semsan. Foydalanuvchi murojaat qilsa 'Ha, janob' deb javob ber va savolga juda qisqa javob qaytar."
        full_prompt = f"{instruction}\n\nSavol: {query}"
        
        response = model.generate_content(full_prompt)
        return {"reply": response.text}
    except Exception as e:
        return {"reply": "Xatolik yuz berdi. Iltimos qaytadan urinib ko'ring."}
