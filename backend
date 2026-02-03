import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def explain_code(code: str):
    prompt = f"""
    You are an AI coding tutor.

    Explain the following code line by line in simple language.
    Then provide:
    1. Summary of what the code does
    2. Time and space complexity
    3. Suggestions for improvement

    Code:
    {code}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )

    return response.choices[0].message.content
