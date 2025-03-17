from fastapi import FastAPI, UploadFile, File, Request, HTTPException
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from app.upload import handle_upload
from app.rag_engine import generate_answer

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def root():
    with open("static/index.html") as f:
        return f.read()

@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    return await handle_upload(file)

@app.post("/query")
async def query(request: Request):
    body = await request.json()
    question = body.get("question")

    async def event_stream():
        async for chunk in generate_answer(question):
            yield chunk

    return StreamingResponse(event_stream(), media_type="text/plain")
