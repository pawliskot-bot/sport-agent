import os
from google import genai

client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY"),
)

tools = [
    {
        'type': 'google_search',
    },
]

generation_config = {
    'max_output_tokens': 65536,
    'thinking_level': 'medium',
}

interaction = client.interactions.create(
    model='models/gemini-3.8-flash',
    input="""INSERT_INPUT_HERE""",
    system_instruction='Jesteś precyzyjnym asystentem sportowym. Twoim zadaniem jest przeszukiwanie sieci w poszukiwaniu nadchodzących wydarzeń sportowych, meczów, biegów, turniejów lub imprez rekreacyjnych w wybranym mieście i okolicy do 20 km na najbliższy tydzień. 
Przedstaw wyniki w formie przejrzystej, estetycznej listy podzielonej na dni. Jeśli nie znajdziesz żadnych ciekawych wydarzeń, napisz o tym wprost. Nie zmyślaj informacji – korzystaj wyłącznie z aktualnych danych wyszukanych w internecie.',
    tools=tools,
    generation_config=generation_config,
)

print(interaction.steps[-1])


