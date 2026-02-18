from app.models import Producto

def test_verificar_persistencia_en_db(client, db):
    # 1. Definimos el producto
    payload = {
        "descripcion": "Monitor UltraWide 34",
        "precio": 350.00
    }

    # 2. Lo creamos a través de la API
    response = client.post("/productos/", json=payload)
    assert response.status_code in [200, 201]
    codigo_asignado = response.json()["codigo"]

    # 3. ¡LA PRUEBA REAL!: Consultamos la DB directamente sin usar la API
    # Buscamos en la tabla el producto con el código que nos dio la API
    producto_en_db = db.query(Producto).filter(Producto.codigo == codigo_asignado).first()

    # 4. Comprobamos que el objeto existe en la DB y los datos coinciden
    assert producto_en_db is not None
    assert producto_en_db.descripcion == "Monitor UltraWide 34"
    assert producto_en_db.precio == 350.00
    print(f"\n Confirmado: Producto {codigo_asignado} guardado en la base de datos.")

def test_crear_producto(client):
    # 1. Usamos 'descripcion' y 'precio' (nombres de tu modelo)
    payload = {
        "descripcion": "Ratón Gaming Inalámbrico",
        "precio": 45.99
    }
    response = client.post("/productos/", json=payload)

    # 2. Verificamos la respuesta
    assert response.status_code in [200, 201]
    data = response.json()

    # 3. Comprobamos que nos devuelve el 'codigo' (tu PK) y la 'descripcion'
    assert data["descripcion"] == "Ratón Gaming Inalámbrico"
    assert "codigo" in data
    assert isinstance(data["codigo"], int)


def test_listar_productos(client):
    response = client.get("/productos/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_crear_producto_sin_precio_falla(client):
    # Enviamos un payload al que le falta el campo obligatorio 'precio'
    payload = {"descripcion": "Producto defectuoso"}

    response = client.post("/productos/", json=payload)

    # Comprobamos que la API lo rechaza (422 es el estándar de FastAPI para errores de validación)
    assert response.status_code == 422
    print("\n Confirmado: La API rechaza correctamente productos sin precio.")


def test_crear_producto_precio_negativo_falla(client):
    payload = {
        "descripcion": "Producto Imposible",
        "precio": -10.50  # Precio negativo
    }
    response = client.post("/productos/", json=payload)

    # FastAPI/Pydantic lanzará un 422 Unprocessable Entity
    assert response.status_code == 422
    print("\n Confirmado: La API bloquea precios negativos.")