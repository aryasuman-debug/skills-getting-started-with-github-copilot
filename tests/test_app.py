import pytest


def test_root_redirect(client):
    """Test GET / redirects to /static/index.html."""
    # Arrange
    # No special setup needed

    # Act
    response = client.get("/")

    # Assert
    assert response.status_code == 200
    assert "<!DOCTYPE html>" in response.text
    assert "Mergington High School" in response.text


def test_get_activities(client):
    """Test GET /activities returns the activities dictionary."""
    # Arrange
    # Activities are predefined in app

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data
    assert "Programming Class" in data
    # Check structure
    activity = data["Chess Club"]
    assert "description" in activity
    assert "schedule" in activity
    assert "max_participants" in activity
    assert "participants" in activity
    assert isinstance(activity["participants"], list)


def test_signup_success(client):
    """Test successful signup for an activity."""
    # Arrange
    activity_name = "Chess Club"
    email = "newstudent@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity_name}/signup?email={email}")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert f"Signed up {email} for {activity_name}" in data["message"]


def test_signup_duplicate(client):
    """Test signup fails if student is already signed up."""
    # Arrange
    activity_name = "Programming Class"
    email = "emma@mergington.edu"  # Already in participants

    # Act
    response = client.post(f"/activities/{activity_name}/signup?email={email}")

    # Assert
    assert response.status_code == 400
    data = response.json()
    assert "detail" in data
    assert "already signed up" in data["detail"]


def test_signup_invalid_activity(client):
    """Test signup fails for non-existent activity."""
    # Arrange
    activity_name = "NonExistent Activity"
    email = "student@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity_name}/signup?email={email}")

    # Assert
    assert response.status_code == 404
    data = response.json()
    assert "detail" in data
    assert "Activity not found" in data["detail"]


def test_remove_participant_success(client):
    """Test successful removal of a participant."""
    # Arrange
    activity_name = "Gym Class"
    email = "john@mergington.edu"  # Already in participants

    # Act
    response = client.delete(f"/activities/{activity_name}/participants?email={email}")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert f"Removed {email} from {activity_name}" in data["message"]


def test_remove_participant_not_found(client):
    """Test removal fails if participant not in activity."""
    # Arrange
    activity_name = "Chess Club"
    email = "nonexistent@mergington.edu"

    # Act
    response = client.delete(f"/activities/{activity_name}/participants?email={email}")

    # Assert
    assert response.status_code == 404
    data = response.json()
    assert "detail" in data
    assert "Participant not found" in data["detail"]


def test_remove_participant_invalid_activity(client):
    """Test removal fails for non-existent activity."""
    # Arrange
    activity_name = "Invalid Activity"
    email = "student@mergington.edu"

    # Act
    response = client.delete(f"/activities/{activity_name}/participants?email={email}")

    # Assert
    assert response.status_code == 404
    data = response.json()
    assert "detail" in data
    assert "Activity not found" in data["detail"]