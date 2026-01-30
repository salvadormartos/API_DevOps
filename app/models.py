from sqlalchemy import Column, Integer, String, Float
from database import Base

class Producto(Base):
    __tablename__ = "productos"

    codigo = Column(Integer, primary_key=True, index=True, autoincrement=True)  #se genera automáticamente
    descripcion = Column(String(100), nullable=False)
    prioridad = Column(String)
    precio = Column(Float, nullable=False)