from fastapi import UploadFile
from app.utils import extract_text_from_pdf, extract_text_from_html, remove_text_after_references
from app.search_index import index_document
from app.utils import chunk_text

async def handle_upload(file: UploadFile):
    content = await file.read()
    filename = file.filename.lower()

    if filename.endswith(".pdf"):
        text = extract_text_from_pdf(content)
    elif filename.endswith(".html") or filename.endswith(".htm"):
        text = extract_text_from_html(content)
    else:
        return {"error": "Unsupported file type. PDF and HTML are supported. File extension must ends with '.pdf', '.html' or '.htm'."}
    
    text = remove_text_after_references(text)

    chunks = chunk_text(text, max_words=32)
    for chunk in chunks:
        index_document(chunk)

    return {"message": f"File \"{file.filename}\" uploaded successfully"}
