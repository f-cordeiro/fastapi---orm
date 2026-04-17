#Fastapi
# pip install fastapi uvicorn jinja2 python-multipart

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

#Para salvar o css em outra pasta
from fastapi.staticfiles import StaticFiles

#Rodar o servidor: python -m uvicorn main:app --reload
app = FastAPI(title="Gestão escolar")

#Configurar o diretorio dos html

templates = Jinja2Templates(directory="templates")

#Mapeia a pasta static para servir arquivos (CSS, IMG, Js)
app.mount("/static", StaticFiles(directory="static"), name ="static")

#Abrir/retornar html:
#metodo HTTP - GET, POST, PUT, DELETE
#GET = Pegar / Listar / Exibir
#POST = Criar / Adicionar
#PUT = Atualizar
#DELETE = Deletar

@app.get("/")
def pagina_inicial(request: Request) :
    return templates.TemplateResponse(
        request, 
        "pagina_inicial.html",
        {"request": request}
    )

@app.get("/alunos")
def listar_alunos(request: Request) :
    alunos = [
        {"nome": "Rayssa", "nota": 5},
        {"nome": "Felipe", "nota": 7},
        {"nome": "yago", "nota": 8},
        {"nome": "Jessica", "nota": 10},
    ]
    return templates.TemplateResponse(
        request,
        "alunos.html",
        {"request": request, "alunos": alunos}
    )

