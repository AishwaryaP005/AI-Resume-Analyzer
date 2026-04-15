import pytest
import os
import sys
from backend.app import extract_skills, recommend_jobs, app

# Fix import path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))




# ---------- UNIT TESTS ----------

def test_extract_skills_basic():
    text = "I know Python and SQL"
    result = extract_skills(text)

    assert isinstance(result, list)
    assert "Python" in result
    assert "Sql" in result


def test_extract_skills_empty():
    result = extract_skills("")
    assert result == []


def test_extract_skills_no_match():
    result = extract_skills("Cooking gardening dancing")
    assert result == []


def test_recommend_jobs_backend():
    jobs = recommend_jobs(["Python"])
    assert "Backend Developer" in jobs


def test_recommend_jobs_frontend():
    jobs = recommend_jobs(["HTML", "JavaScript"])
    assert "Frontend Developer" in jobs


def test_recommend_jobs_default():
    jobs = recommend_jobs([])
    assert "Software Engineer" in jobs


# ---------- API TESTS ----------

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home_route(client):
    response = client.get("/")
    assert response.status_code == 200


def test_upload_no_file(client):
    response = client.post("/upload")
    assert response.status_code == 400
