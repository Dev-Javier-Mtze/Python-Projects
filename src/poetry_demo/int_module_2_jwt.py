from fastapi import FastAPI, HTTPException

fake_users_db = {"alice": "1234"}
app = FastAPI()


@app.post("/login")
def login(username: str, password: str):
    if fake_users_db.get(username) != password:
        raise HTTPException(status_code=400, detail="Credenciales inválidas")
    else:
        print("Login successful")


try:
    login("alice", "1234")
except Exception as e:
    print(f"{e}")
