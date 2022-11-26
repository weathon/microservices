from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "I am glad you are here, we have some cookies, come here!"}


