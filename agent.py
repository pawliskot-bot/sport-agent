import json
import os
import urllib.parse
import urllib.request
from google import genai
from google.genai import types

# 1. Inicjalizacja klienta Gemini
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

# 2. Generowanie raportu przez model z wykorzystaniem wyszukiwarki
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=(
        "Znajdź nadchodzące wydarzenia sportowe w mieście Oława na najbliższe"
        " dni."
    ),
    config=types.GenerateContentConfig(
        tools=[types.Tool(google_search=types.GoogleSearch())],
        system_instruction=(
            "Jesteś precyzyjnym asystentem sportowym. Twoim zadaniem jest"
            " przeszukiwanie sieci w poszukiwaniu nadchodzących wydarzeń"
            " sportowych, meczów, biegów, turniejów lub imprez rekreacyjnych w"
            " wybranym mieście i okolicy na najbliższy tydzień. Przedstaw wyniki"
            " w formie przejrzystej, estetycznej listy podzielonej na dni. Jeśli"
            " nie znajdziesz żadnych ciekawych wydarzeń, napisz o tym wprost."
            " Nie zmyślaj informacji – korzystaj wyłącznie z aktualnych danych"
            " wyszukanych w internecie."
        ),
    ),
)

report_text = response.text
print("=== WYGENEROWANY RAPORT ===")
print(report_text)

# 3. Wysyłanie powiadomienia na Telegram
TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

if TOKEN and CHAT_ID:
  url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
  payload = {
      "chat_id": CHAT_ID,
      "text": f"⚽ **Raport Sportowy - Oława** ⚽\n\n{report_text}",
      "parse_mode": "Markdown",
  }

  data = urllib.parse.urlencode(payload).encode("utf-8")
  req = urllib.request.Request(url, data=data, method="POST")

  try:
    with urllib.request.urlopen(req) as f:
      print("Powiadomienie na Telegram zostało wysłane pomyślnie!")
  except Exception as e:
    print(f"Błąd podczas wysyłania wiadomości na Telegram: {e}")
else:
  print("Brak skonfigurowanych danych Telegrama w zmiennych środowiskowych.")
