from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline
import re

# Initialize FastAPI app
app = FastAPI(title="Financial Assistant API")

# Define request and response schemas
class QuestionRequest(BaseModel):
    question: str

class AnswerResponse(BaseModel):
    answer: str

# Load lightweight text generation pipeline
generator = pipeline("text2text-generation", model="google/flan-t5-base")

# Basic bad words for moderation
BANNED_WORDS = ["kill", "hack", "bomb", "drugs", "weapon", "suicide"]

# Function to check for banned content
def contains_banned_words(text):
    text = text.lower()
    return any(word in text for word in BANNED_WORDS)

# POST endpoint
@app.post("/ask", response_model=AnswerResponse)
def ask_question(request: QuestionRequest):
    question = request.question.strip()

    # Guardrail: reject empty or unsafe input
    if not question:
        raise HTTPException(status_code=400, detail="Question cannot be empty.")
    if contains_banned_words(question):
        raise HTTPException(status_code=400, detail="Inappropriate content detected.")

    # Use the instruction-tuned model to generate a relevant answer
    formatted_input = f"Answer this finance question: {question}"
    result = generator(formatted_input, max_length=100, num_return_sequences=1)
    answer = result[0]["generated_text"].strip()

    # Fallback if model fails
    if not answer:
        answer = "I'm sorry, I couldn't generate a response."

    return {"answer": answer}


