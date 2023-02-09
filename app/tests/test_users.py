"""
Archivo para hacer pruebas de los diferentes servicios.
"""

from fastapi.testclient import TestClient
# from api.main import app
from app.main import app


client = TestClient(app.router)


def test_root():
    """
    Función para test de la ruta / de usuarios.
    :return:
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Up and running!"}
