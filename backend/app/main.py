from fastapi import FastAPI

app = FastAPI(title="Elysia API - placeholder")

@app.get("/")
def root():
    return {"status": "ok"}
