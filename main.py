from fastapi import FastAPI, File, UploadFile
from PyPDF2 import PdfFileReader
import io

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "I am glad you are here, we have some cookies, come here!"}


@app.post("/contractKeywordChecking")
async def contract(file: UploadFile):
    parts=[]
    def visitor_body(text, cm, tm, fontDict, fontSize):
        parts.append(text)

    request_object_content = await file.read()
    pdf = PdfFileReader(io.BytesIO(request_object_content))
    pages = pdf.pages

    for i in pages:
        i.extract_text(visitor_text=visitor_body)
    words = []
    for i in parts:
        tmp = i.split(" ")
        for j in tmp:
            if j!= "" and j!="\n":
                word = ''.join(c for c in j.lower() if (48<=ord(c)<=57 or 97<=ord(c)<=122))
                words.append(word)
    print(words[:100])
    return {
        "Number of Pages":len(pages),
        "Warnings": 0
    }
