from sqlalchemy.orm import Session
from src.db import models, schemas
from src.db.database import get_db


def conn_db(func):
    def wrapper(*args):
        with get_db() as db:
            retorno = func(*args, db=db)
        return retorno

    return wrapper


@conn_db
def cria_registro(registro: schemas.CriaRegistro, db: Session):
    db_registro = models.AnaliseCadastro(**registro)
    db.add(db_registro)
    db.commit()
    db.refresh(db_registro)
    return db_registro.id


@conn_db
def cria_controle(controle: schemas.CriaControle, db: Session):
    db_controle = models.ControleAnaliseCadastro(**controle)
    db.add(db_controle)
    db.commit()
    db.refresh(db_controle)
    return db_controle.id


@conn_db
def consulta_fila(db: Session):
    dados_cadastrais = (
        db.query(models.AnaliseCadastro, models.ControleAnaliseCadastro)
        .join(
            models.ControleAnaliseCadastro,
            models.AnaliseCadastro.id
            == models.ControleAnaliseCadastro.id_controle_analise,
        )
        .filter(
            models.ControleAnaliseCadastro.dado_cadastrado == 0,
        )
        .all()
    )
    return dados_cadastrais


@conn_db
def atualiza_status_controle(id: int, campos_atualizacao: dict, db: Session):
    db_dados = db.query(models.ControleAnaliseCadastro).filter(
        models.ControleAnaliseCadastro.id_controle_analise == id
    )
    db_dados.update(campos_atualizacao)
    db.commit()
    return True
