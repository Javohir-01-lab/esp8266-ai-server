from fastapi import FastAPI
import requests

app = FastAPI()

# MA'LUMOTLAR
GROQ_API_KEY = "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"
TELEGRAM_TOKEN = "8654947812:AAHe-zuEdL0rob1v6M_v5f85P8IypbCDvf8"
CHAT_ID = "8565555123" # @userinfobot orqali bilib oling

@app.get("/ask")
def ask_ai(query: str):
    try:
        # 1. AI-dan javob olish
        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
       payload = {
            "model": "llama-3.1-70b-versatile", # Kuchliroq va aqlliroq model (70B)
            "messages": [
                {
                    "role": "system", 
                    "content": """Sening isming Sem. Sen kuchli muhandissan va Javohirning eng yaqin yordamchisan. 
                    Robot kabi 'Salom, nima yordam kerak' deb gapirma. 
                    Mantiqiy, do'stona va xuddi odamdek gaplash. Muhandislik masalalarida o'z fikringni bildir. 
                    Javoblaring qisqa, lekin mazmunli bo'lsin."""
                },
                {"role": "user", "content": query}
            ],
            "temperature": 0.7, # Bu parametr AIni ijodiyroq va jonliroq qiladi
        }
        }
        response = requests.post(url, json=payload, headers=headers)
        answer = response.json()["choices"][0]["message"]["content"]

        # 2. Telegramga yuborish (Sizga qulay bo'lishi uchun)
        tg_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        requests.post(tg_url, json={"chat_id": CHAT_ID, "text": f"🤖 Sem: {answer}"})

        return answer
    except Exception as e:
        return f"Xato: {str(e)}"
