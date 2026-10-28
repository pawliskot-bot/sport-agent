import os
from google import genai
from google.genai import types

# Inicjalizacja klienta przy użyciu sekretu z GitHuba
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

# Wywołanie modelu Gemini z włączonym wyszukiwaniem Google
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

print("=== RAPORT SPORTOWY ===")
print(response.text)
