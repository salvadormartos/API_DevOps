from pydantic import BaseModel, Field

class ProductoBase(BaseModel):
    descripcion: str = Field(min_length=3, max_length=100)
    precio: float = Field(gt=0)

# Para crear un producto
class ProductoCreate(ProductoBase):
    pass

class ProductoUpdate(ProductoBase):
    pass

class ProductoOut(ProductoBase):
    codigo: int
    class Config:
        from_attributes = True  # permite convertir objetos ORM a Pydantic