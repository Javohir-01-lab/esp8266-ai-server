from fastapi import FastAPI
import google.generativeai as genai

app = FastAPI()

# API kaliti
GOOGLE_API_KEY = "AIzaSyCZTpdwJzQ8a85JGD491l1ygDZtNiD3ZhY"
genai.configure(api_key=GOOGLE_API_KEY)

# Modelni eng sodda ko'rinishda chaqiramiz
model = genai.GenerativeModel('gemini-1.5-flash')

@app.get("/")
def home():
    return {"message": "Server ishlayapti!"}

@app.get("/ask")
def ask_ai(query: str):
    try:
        response = model.generate_content(f"Sen yordamchi Semsan. Javobing qisqa bo'lsin. Savol: {query}")
        return {"reply": response.text}
    except Exception as e:
        # Bu yerda xatoni matn ko'rinishida qaytaramiz
        return {"reply": f"API Xatosi: {str(e)}"}
