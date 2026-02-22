from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import Base, engine, get_db
from app import crud
from app.schemas import ProductoCreate, ProductoUpdate, ProductoOut

# Esto crea las tablas si no existen
Base.metadata.create_all(bind=engine)
app = FastAPI(title="FastAPI + SQLite", version="1.0.0")

@app.get("/productos", response_model=list[ProductoOut])
def listar_productos(db: Session = Depends(get_db)):
    return crud.get_productos(db)

@app.get("/productos/{codigo}", response_model=ProductoOut)
def obtener_producto(codigo: int, db: Session = Depends(get_db)):
    prod = crud.get_producto(db, codigo)
    if not prod:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return prod

@app.post("/productos", response_model=ProductoOut, status_code=status.HTTP_201_CREATED)
def crear_producto(data: ProductoCreate, db: Session = Depends(get_db)):
    return crud.create_producto(db, data)

@app.put("/productos/{codigo}", response_model=ProductoOut)
def actualizar_producto(codigo: int, data: ProductoUpdate, db: Session = Depends(get_db)):
    prod = crud.update_producto(db, codigo, data)
    if not prod:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return prod

@app.delete("/productos/{codigo}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_producto(codigo: int, db: Session = Depends(get_db)):
    prod = crud.delete_producto(db, codigo)
    if not prod:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return

@app.get("/")
def read_root():
    return {"message": "App API_DevOps v1.0"}