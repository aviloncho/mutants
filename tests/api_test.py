from pathlib import Path
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.database import Base
from main_api import app, get_db
from tests import fixtures

test_db_file = Path.cwd() / 'test.db'
if test_db_file.exists():
    test_db_file.unlink()

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False,
                                   autoflush=False,
                                   bind=engine)


Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def test_root():
    response = client.get('/')
    assert response.status_code == 200, response.text
    data = response.json()
    assert 'message' in data
    assert data['message'] == 'Welcome to DNA Analysis'


def request_mutant(request_dna, expected_status_code=200):
    response = client.post(
        '/mutant/',
        json={'dna': request_dna},
    )
    assert response.status_code == expected_status_code
    assert response.text
    data = response.json()
    assert data['dna'] == request_dna
    assert 'dna_hash' in data

    return data['dna_hash']


def test_mutant():
    dna_hash = request_mutant(fixtures.EXAMPLE)

    response = client.get(f'/dnas/{dna_hash}')
    assert response.status_code == 200, response.text
    data = response.json()
    assert data
    assert data['dna_hash'] == dna_hash

    request_mutant(fixtures.EXAMPLE)


def test_human():
    response = client.post(
        '/mutant/',
        json={'dna': fixtures.HUMAN},
    )
    assert response.status_code == 403, response.text
    data = response.json()
    assert data['dna'] == fixtures.HUMAN
    assert 'dna_hash' in data

    request_mutant(fixtures.HUMAN, 403)


def test_dnas():
    response = client.get('/dnas/')
    assert response.status_code == 200, response.text


def test_dnas_nonexistent_dna():
    response = client.get('/dnas/nonexistent-dna')
    assert response.status_code == 200, not response.text


def test_stats():
    response = client.get('/stats/')
    assert response.status_code == 200, response.text
    data = response.json()
    assert 'count_mutant_dna' in data
    assert 'count_human_dna' in data
    assert 'ratio' in data
