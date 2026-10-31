
import sqlite3

def login(username, password):
    query = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'"
    return query

def add(a, b):
    return a + b

if __name__ == "__main__":
    print("Sample Jenkins Security Application")
    print("Addition:", add(10, 20))
