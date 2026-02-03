from fastapi import FastAPI
from pydantic import BaseModel
from ai_engine import explain_code
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CodeRequest(BaseModel):
    code: str

@app.post("/explain")
def explain(request: CodeRequest):
    explanation = explain_code(request.code)
    return {"result": explanation}
