import pytest
from app import app, db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_data(client):
    """Проверка, что эндпоинт /api/data доступен"""
    res = client.get('/api/data')
    assert res.status_code == 200
