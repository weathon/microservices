from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "I am glad you are here, we have some cookies, come here!"}


@app.get("/contractKeywordChecking")
async def contract(file: UploadFile):
    return {"message": "I am glad you are here, we have some cookies, come here!"}
