import pytest
from fastapi.testclient import TestClient
from src.app import app, activities

# Initial activities data for reset
initial_activities = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
    "Basketball Team": {
        "description": "Competitive basketball training and matches",
        "schedule": "Mondays and Wednesdays, 4:00 PM - 5:30 PM",
        "max_participants": 15,
        "participants": ["james@mergington.edu"]
    },
    "Tennis Club": {
        "description": "Tennis lessons and practice sessions",
        "schedule": "Tuesdays and Thursdays, 4:30 PM - 5:30 PM",
        "max_participants": 8,
        "participants": ["lucas@mergington.edu", "ava@mergington.edu"]
    },
    "Art Studio": {
        "description": "Painting, drawing, and visual art projects",
        "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 15,
        "participants": ["isabella@mergington.edu"]
    },
    "Drama Club": {
        "description": "Theater, acting, and stage performance",
        "schedule": "Thursdays, 3:30 PM - 5:00 PM",
        "max_participants": 20,
        "participants": ["noah@mergington.edu", "mia@mergington.edu"]
    },
    "Debate Team": {
        "description": "Develop argumentation and public speaking skills",
        "schedule": "Mondays and Fridays, 3:30 PM - 4:30 PM",
        "max_participants": 10,
        "participants": ["alex@mergington.edu"]
    },
    "Science Club": {
        "description": "Conduct experiments and explore scientific concepts",
        "schedule": "Wednesdays, 4:00 PM - 5:00 PM",
        "max_participants": 18,
        "participants": ["grace@mergington.edu", "lucas@mergington.edu"]
    }
}


@pytest.fixture
def client():
    """TestClient fixture for FastAPI app."""
    # Reset activities to initial state before each test
    activities.clear()
    activities.update(initial_activities)
    return TestClient(app)