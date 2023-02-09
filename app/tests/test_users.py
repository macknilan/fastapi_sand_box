"""
Archivo para hacer pruebas de los diferentes servicios.
"""

from fastapi.testclient import TestClient
# from api.main import app
# from app.main import app
from app import app

client = TestClient(app.router)


def test_home():
    """
    Función para test de la ruta / de usuarios.
    :return:
    """
    response = client.get("users/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}
