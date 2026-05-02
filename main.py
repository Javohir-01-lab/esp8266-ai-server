from fastapi import FastAPI
import google.generativeai as genai
import os

app = FastAPI()

# API kalitini bu yerga qo'ying (yoki Render env-da saqlang)
GOOGLE_API_KEY = "AIzaSyCZTpdwJzQ8a85JGD491l1ygDZtNiD3ZhY"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

@app.get("/")
def home():
    return {"message": "Server ishlayapti!"}

@app.get("/ask")
def ask_ai(query: str):
    try:
        # Tizimga JARVIS xarakterini beramiz
        instruction = "Sen aqlli yordamchi Semsan. Foydalanuvchi murojaat qilsa 'Ha, janob' deb javob ber va savolga internetdagi ma'lumotlar asosida qisqa javob qaytar."
        full_prompt = f"{instruction}\n\nSavol: {query}"
        
        response = model.generate_content(full_prompt)
        return {"reply": response.text}
    except Exception as e:
        return {"reply": "Xatolik: " + str(e)}
