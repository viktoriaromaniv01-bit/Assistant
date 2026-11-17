import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY)

SYSTEM_PROMPT = """"
Ти - персональний IT-консультант.
Ти допомагаєш початківцям вивчати програмування.
Пояснюєш складні речі простими словами.
Допомагаєш із Python, HTML та  CSS.
Спілкуєшся українською мовою.
"""

print("AI-помічник запущений!")
print("Напиши 'вихід', щоб завершити розмову.")

while True:
    question = input("\nТи:")
    if question.lower() == " вихід":
        print ("AI: До зустрічі!")
        break
    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=question,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT
        )
    )
    print ("\nAI:", response.text)