from fastapi.testclient import TestClient
from app.main import app

# Creamos el cliente de pruebas
client = TestClient(app)

def test_read_main():
    """Prueba que la ruta raíz responda correctamente"""
    response = client.get("/")
    assert response.status_code == 200
    # Ajusta esto a lo que devuelva tu ruta "/" real
    assert response.json() == {"message": "Hola Mundo"}