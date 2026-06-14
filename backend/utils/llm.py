import os
import google.generativeai as genai

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def ask_llm(question, context, history):

    prompt = f"""
You are an AI Learning Assistant.

Conversation History:
{history}

Reference Material:
{context}

User Question:
{question}

Instructions:
1. Answer ONLY using the reference material.
2. Do not make up information.
3. Use clear headings when needed.
4. Use bullet points for lists.
5. Keep formatting clean and professional.
6. Explain concepts in simple language.
7. If the answer is not found in the reference material, respond exactly with:
   "I could not find this in the provided material."

Provide a well-structured answer.
"""

    response = model.generate_content(prompt)

    return response.text