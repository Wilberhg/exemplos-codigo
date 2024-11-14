from sqlalchemy import Column, String, DateTime, Integer, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from src.db.database import engine
from datetime import datetime


Base = declarative_base()


class AnaliseCadastro(Base):
    __tablename__ = "TB_AnaliseCadastro"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(length=30), nullable=False)
    last_name = Column(String(length=30), nullable=False)
    company_name = Column(String(length=30), nullable=False)
    role_company = Column(String(length=30), nullable=False)
    address = Column(String(length=50), nullable=False)
    email = Column(String(length=30), nullable=False)
    phone_number = Column(String(length=11), nullable=False)
    data_carga = Column(DateTime(), default=datetime.now, nullable=False)
    analise = relationship("ControleAnaliseCadastro", back_populates="controle")


class ControleAnaliseCadastro(Base):
    __tablename__ = "TB_ControleAnaliseCadastro"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_controle_analise = Column(
        Integer, ForeignKey("TB_AnaliseCadastro.id"), nullable=False
    )
    dado_cadastrado = Column(Boolean(), default=False, nullable=False)
    data_atualizacao = Column(DateTime, onupdate=datetime.now, nullable=True)
    controle = relationship("AnaliseCadastro", back_populates="analise")


Base.metadata.create_all(bind=engine)
