from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from modules.generate_qr_code import generate_qr_code

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get('/')
def home():
    return {'status': 'succeed'}


@app.get("/get_qr_code")
async def get_qr_code(request: Request, url="", response_type="json"):
    qr_code = generate_qr_code(url)
    context = {"qr_code": qr_code}

    if response_type == "html":
        context["request"] = request
        return templates.TemplateResponse("qr_code.html", context)
    return context

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)
