from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Cliente(Base):
    __tablename__ = "clientes"

    id_cliente = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    estado = Column(String, nullable=False)

    processos = relationship("Processo", back_populates="cliente")

class Processo(Base):
    __tablename__ = "processos"

    id_processo = Column(Integer, primary_key=True)
    id_cliente = Column(Integer, ForeignKey("clientes.id_cliente"), nullable=False)
    assunto = Column(String, nullable=False)
    data_abertura = Column(Date, nullable=False)

    cliente = relationship("Cliente", back_populates="processos")