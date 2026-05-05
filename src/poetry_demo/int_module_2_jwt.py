from fastapi import FastAPI, HTTPException

from poetry_demo.utils import logging_console_file

fake_users_db = {"ricardo": "0202"}
app = FastAPI()


@app.post("/login")
def login(username: str, password: str):
    if fake_users_db.get(username) != password:
        raise HTTPException(status_code=400, detail="Bad credentials")
    else:
        logger.debug("Login successful")


if __name__ == "__main__":
    logger = logging_console_file.logging_file("int_module_2_jwt")
    logger.info(" - - - - - - Start of the test - - - - - - ")
    try:
        login("ricardo", "0202")
    except Exception as e:
        print(f"{e}")
