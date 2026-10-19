from app.main import health_check, add_numbers


def test_health_check():
    assert health_check() == {"status": "healthy"}


def test_add_numbers():
    assert add_numbers(2, 3) == 5


def test_add_negative_numbers():
    assert add_numbers(-2, -3) == -5
