
from app import add, login

def test_add():
    assert add(10, 20) == 30

def test_add_zero():
    assert add(5, 0) == 5

def test_login_query():
    result = login("admin", "1234")
    assert "SELECT" in result
