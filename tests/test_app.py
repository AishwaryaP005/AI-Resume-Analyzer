import sys
import os

# Fix import path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.app import extract_skills, recommend_jobs, app
import pytest

# --- Unit Tests ---

def test_extract_skills_basic():
    text = "I have experience in Python and SQL"
    result = extract_skills(text)

    assert "Python" in result
    assert "Sql" in result  # because .title() → Sql


def test_extract_skills_empty():
    result = extract_skills("")
    assert result == []


def test_extract_skills_no_match():
    result = extract_skills("I love cooking and gardening")
    assert result == []


def test_recommend_jobs_python():
    jobs = recommend_jobs(["Python"])
    assert "Backend Developer" in jobs


def test_recommend_jobs_frontend():
    jobs = recommend_jobs(["HTML", "JavaScript"])
    assert "Frontend Developer" in jobs


def test_recommend_jobs_ml():
    jobs = recommend_jobs(["Machine Learning"])
    assert "Data Scientist" in jobs


def test_recommend_jobs_empty():
    result = recommend_jobs([])
    assert "Software Engineer" in result


# --- API Tests ---

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
    data = response.get_json()
    assert "error" in data
