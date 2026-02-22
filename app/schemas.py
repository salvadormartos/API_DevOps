from pydantic import Field, BaseModel, ConfigDict # Importa ConfigDict

class ProductoBase(BaseModel):
    descripcion: str = Field(min_length=3, max_length=100)
    #precio: float = Field(gt=0, description="El precio debe ser mayor que cero")
    precio: float = Field()

# Para crear un producto
class ProductoCreate(ProductoBase):
    pass

class ProductoUpdate(ProductoBase):
    pass

class ProductoOut(ProductoBase):
    codigo: int
    # Esto es vital para que Pydantic entienda a SQLAlchemy
    model_config = ConfigDict(from_attributes=True) # Nueva forma
