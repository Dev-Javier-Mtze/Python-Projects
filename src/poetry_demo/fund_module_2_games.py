import json
import os

from poetry_demo.utils import base_dir, logging_console_file


def add_game_id():
    try:
        game_id = int(input("Give me a number between 1-9999\n"))
        return validate_game_id(game_id)
    except ValueError:
        logger.warning("Not a valid id")
        return False


def validate_game_id(game_id):
    if game_id < 1 or game_id > 9999:
        logger.warning("Not a valid id")
        return

    return game_id


def add_game_file(game_id):

    try:
        if (
            os.path.join(base_dir.url_dir(), "data", "games.json")
            and os.path.getsize(f"{base_dir.url_dir()}/data/games.json") > 0
        ):
            with open(f"{base_dir.url_dir()}/data/games.json", "r") as file:
                data = json.load(file)
                result = data.get(str(game_id), False)

                if result:
                    logger.debug("Game already in the library")
                    logger.debug(
                        f"Your game is {result['name']} with a rating of {result['rating']}"
                    )
                    return data
                else:
                    return add_game_data(data)
        else:
            return add_game_data()
    except Exception as e:
        print(e)
        return add_game_data()


def add_game_data(data={}):
    game_name = input("Could you give me the name of the game?\n")
    try:
        game_rating = int(input("Could you give me a rating between 1-10?\n"))

    except ValueError:
        logger.warning("Invalid rating")
        return

    if game_rating < 1 or game_rating > 10:
        logger.warning("Invalid rating")
        return

    data[game_id] = {"name": game_name, "rating": game_rating}

    json_string = json.dumps(data, indent=4)
    with open(f"{base_dir.url_dir()}/data/games.json", "w") as file:
        file.write(json_string)

    logger.debug("Your game is now in the library")
    with open(f"{base_dir.url_dir()}/data/games.json", "r") as file:
        data = json.load(file)
        return data


def retrieve_game_rating(data):
    good_rating = [game for game in data.values() if game["rating"] >= 8]
    logger.debug("The games that we found above 7 in rating are:")

    for game in good_rating:
        logger.debug(f"Name: {game['name']} with a rating of {game['rating']}")


if __name__ == "__main__":
    logger = logging_console_file.logging_file("fund_module_2_games")
    logger.info(" - - - - - - Start of the test - - - - - - ")
    game_id = add_game_id()
    if game_id:
        json_data = add_game_file(game_id)
        retrieve_game_rating(json_data)
