import os
import json
import re

USERS_FILE = "users.json"
HISTORY_FILE = "history.json"

def init_users():
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, "w") as f:
            json.dump({}, f)
    if not os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "w") as f:
            json.dump({}, f)

def is_valid_password(password):
    if len(password) < 8:
        return False, "Password minimal 8 karakter."
    if not re.search(r"[A-Za-z]", password):
        return False, "Password harus mengandung huruf."
    if not re.search(r"\d", password):
        return False, "Password harus mengandung angka."
    return True, ""

def register_user(username, password):
    init_users()
    with open(USERS_FILE, "r") as f:
        users = json.load(f)

    if username in users:
        return False, "Username sudah terdaftar."

    valid, message = is_valid_password(password)
    if not valid:
        return False, message

    users[username] = password
    with open(USERS_FILE, "w") as f:
        json.dump(users, f)
    return True, "Pendaftaran berhasil."

def login(username, password):
    init_users()
    with open(USERS_FILE, "r") as f:
        users = json.load(f)
    return users.get(username) == password

def save_history(username, label):
    init_users()
    with open(HISTORY_FILE, "r") as f:
        history = json.load(f)
    if username not in history:
        history[username] = []
    history[username].append(label)
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f)

def get_history(username):
    init_users()
    with open(HISTORY_FILE, "r") as f:
        history = json.load(f)
    return history.get(username, [])
