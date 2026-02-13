from google import genai
from config import GEMINI_API_KEY
from prompts import IMPROVED_PROMPT

client = genai.Client(api_key=GEMINI_API_KEY)

def generate_answer(question, retrieved_chunks):

    context = "\n\n".join(retrieved_chunks)

    prompt = IMPROVED_PROMPT.format(
        context=context,
        question=question
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text
