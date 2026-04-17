from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

class Curso(Base):
    __tablename__ = "cursos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    duracao_dias = Column(Integer)
    descricao = Column(String(100))

    alunos = relationship("Aluno", back_populates="curso")

class Aluno(Base):
    __tablename__ = "alunos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), unique=True)
    idade = Column(Integer)

    curso_id = Column(Integer, ForeignKey("cursos.id"))

    curso = relationship("Curso", back_populates="alunos")

engine = create_engine("sqlite:///escola.db")

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

#Criar uma função para conectar ao banco de dados
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

