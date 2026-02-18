from sqlalchemy.orm import Session
from app.models import Producto
from app.schemas import ProductoCreate, ProductoUpdate

def get_productos(db: Session):
    return db.query(Producto).all()

def get_producto(db: Session, codigo: int):
    return db.query(Producto).filter(Producto.codigo == codigo).first()

def create_producto(db: Session, data: ProductoCreate):
    prod = Producto(**data.model_dump())  # SQLite genera el código automáticamente
    db.add(prod)
    db.commit()
    db.refresh(prod)  # refresca para obtener el código asignado
    return prod

def update_producto(db: Session, codigo: int, data: ProductoUpdate):
    prod = get_producto(db, codigo)
    if prod:
        prod.descripcion = data.descripcion
        prod.precio = data.precio
        db.commit()
        db.refresh(prod)
    return prod

def delete_producto(db: Session, codigo: int):
    prod = get_producto(db, codigo)
    if prod:
        db.delete(prod)
        db.commit()
    return prod