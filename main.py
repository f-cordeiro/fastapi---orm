#Fastapi
# pip install fastapi uvicorn jinja2 python-multipart

from fastapi import FastAPI, Request, Depends, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse

#Para salvar o css em outra pasta
from fastapi.staticfiles import StaticFiles
from models import get_db, Curso, Aluno
from sqlalchemy.orm import Session

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

@app.get("/curso/cadastro")
def exibir_cadastro_curso(request: Request):
    return templates.TemplateResponse(
        request,
        "cadastro_curso.html",
        {"request": request}
    )

@app.post("/curso")
def criar_curso(
    nome: str = Form(...),
    duracao_dias: int = Form(...),
    descricao: str = Form(...),
    db: Session = Depends(get_db)
):
    novo_curso = Curso(nome=nome, duracao_dias=duracao_dias, descricao=descricao)
    db.add(novo_curso)
    db.commit()

    return RedirectResponse(url="/", status_code=303)