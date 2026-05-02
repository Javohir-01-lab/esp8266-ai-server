from fastapi import FastAPI
import google.generativeai as genai
import os

app = FastAPI()

# API kaliti
GOOGLE_API_KEY = "AIzaSyCZTpdwJzQ8a85JGD491l1ygDZtNiD3ZhY"
genai.configure(api_key=GOOGLE_API_KEY)

# Modelni aniq va to'g'ri ko'rinishda tanlash
# 'gemini-1.5-flash' modeli hozirda eng tezkor va barqaror hisoblanadi
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

@app.get("/")
def home():
    return {"message": "Sem AI Server ishlayapti!"}

@app.get("/ask")
def ask_ai(query: str):
    try:
        # Tizimga Sem (JARVIS uslubida) xarakterini beramiz
        instruction = "Sen aqlli yordamchi Semsan. Foydalanuvchi murojaat qilsa 'Ha, janob' deb javob ber va savolga juda qisqa javob qaytar."
        
        # Javobni generatsiya qilish
        response = model.generate_content(f"{instruction}\n\nSavol: {query}")
        
        # Javob matnini qaytarish
        return {"reply": response.text}
    except Exception as e:
        # Xatolikni aniq ko'rish uchun terminalga chiqaramiz
        print(f"Xato yuz berdi: {e}")
        return {"reply": "Xatolik: " + str(e)}
