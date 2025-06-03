# Ask a Financial Question – GenAI Assistant

This is a simple financial assistant powered by Generative AI, built with FastAPI and an open-source language model. It answers basic personal finance questions through a single REST API endpoint.

## How to Run the App Locally:

### 1. Install the required packages:

pip install fastapi uvicorn transformers torch

### 2. Run the FastAPI server:

uvicorn main:app --reload

### 3. Open your browser and go to:

http://127.0.0.1:8000/docs


## Why I Picked This Model?
I used the *google/flan-t5-base model* because it’s instruction-tuned, so it gives concise and relevant answers to direct questions. Also, It’s CPU-friendly and runs efficiently on standard machines.


## Few sample questions to try:
"Why should people save money?"  
"How can I build an emergency fund?"  
"How does compound interest work?"  
