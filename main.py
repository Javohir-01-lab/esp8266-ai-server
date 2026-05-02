from fastapi import FastAPI
import google.generativeai as genai

app = FastAPI()

# API kaliti
GOOGLE_API_KEY = "AIzaSyCZTpdwJzQ8a85JGD491l1ygDZtNiD3ZhY"
genai.configure(api_key=GOOGLE_API_KEY)

# Modelni barqaror nom bilan yuklash
model = genai.GenerativeModel('gemini-1.5-flash')

@app.get("/")
def home():
    return {"message": "Server ishlamoqda!"}

@app.get("/ask")
def ask_ai(query: str):
    try:
        # Promptni yuboramiz
        response = model.generate_content(f"Sen Semsan. Savol: {query}")
        
        # Javobni tekshirish
        if response and response.text:
            return {"reply": response.text}
        else:
            return {"reply": "Kechirasiz, javob topilmadi."}
            
    except Exception as e:
        return {"reply": f"API Xatosi: {str(e)}"}
