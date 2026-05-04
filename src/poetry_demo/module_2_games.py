import json
import logging
import os

from logging_config import setup_logging

setup_logging()
logger = logging.getLogger("module_2_games")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)


def add_game_id():
    try:
        game_id = int(input("Give me a number between 1-9999\n"))
        return validate_game_id(game_id)
    except ValueError:
        print("Not a valid id")
        return False


def validate_game_id(game_id):
    if game_id < 1 or game_id > 9999:
        print("Not a valid id")
        return

    print(f"Your id is: {game_id}")
    return game_id


def add_game_file(game_id):

    try:
        if (
            os.path.join(BASE_DIR, "data", "games.json")
            and os.path.getsize(f"{BASE_DIR}/data/games.json") > 0
        ):
            with open(f"{BASE_DIR}/data/games.json", "r") as file:
                data = json.load(file)
                result = data.get(str(game_id), False)

                if result:
                    print("Game already in the library")
                    print(
                        f"Your game is {result['name']} with a rating of {result['rating']}"
                    )
                else:
                    return add_game_data(data)
        else:
            return add_game_data()
    except Exception as e:
        print(e)
        return add_game_data()


def add_game_data(data={}):
    game_name = input("Could you give me the name of the game?")
    try:
        game_rating = int(input("Could you give me a rating between 1-10?"))

    except ValueError:
        print("Invalid rating")
        return

    if game_rating < 1 or game_rating > 10:
        print("Not a valid rating")
        return

    data[game_id] = {"name": game_name, "rating": game_rating}

    json_string = json.dumps(data, indent=4)
    with open(f"{BASE_DIR}/data/games.json", "w") as file:
        file.write(json_string)

    print("Your game is now in the library")
    logger.debug("Game added to the library")
    return json_string


# def retrieve_game_rating(data):
#     result = json.loads(data)
#     print(result)
#     good_rating = [game for game in result if game["rating"] > 8]
#     print(good_rating)


if __name__ == "__main__":
    # Only runs when you execute the script directly, not when imported
    game_id = add_game_id()
    if game_id:
        json_data = add_game_file(game_id)
        # retrieve_game_rating(json_data)
