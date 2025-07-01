from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()

templates = Jinja2Templates(directory=".")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/calculate")
async def calculate(expression: str):
    try:
        result = eval(expression)
        return {"result": result}
    except:
        return {"result": "Error"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
