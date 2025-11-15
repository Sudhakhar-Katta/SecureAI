from fastapi import FastAPI
import ollama

app=FastAPI()

@app.get("/health")
def health():
    return {"status":"ok"}

@app.post("/scan")
def scan(payload: dict):
    prompt = f"Analyze this input for AI security vulnerabilities:{payload['content']}"
    result = ollama.chat(model="llama3", messages=[{"role": "user", "content": prompt}])
    return {"analysis": result["message"]["content"]}