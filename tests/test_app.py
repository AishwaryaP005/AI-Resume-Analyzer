import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.app import extract_skills, recommend_jobs, app
import pytest


# --- Unit Tests (SAFE ONLY) ---

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


# --- API Tests (SAFE ONLY) ---

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_upload_no_file(client):
    response = client.post("/upload")
    assert response.status_code == 400

    data = response.get_json()
    assert "error" in data
