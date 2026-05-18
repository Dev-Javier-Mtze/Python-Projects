import os
from typing import TypedDict

import pandas as pd

from poetry_demo.utils import base_dir, logging_console_file

CSV_URL = f"{os.path.join(base_dir.url_dir(), 'data', 'contact_list.csv')}"


class ContactList(TypedDict):
    Id: dict[int, int]
    Name: dict[int, str]
    Email: dict[int, str]
    Phone: dict[int, str]


def load_cvs():
    result = pd.read_csv(CSV_URL)
    logger.debug(result)
    csv_dict = result.to_dict()
    return csv_dict


def write_csv(csv: ContactList):
    name = input("Give me your name:\n")
    email = input("Give me your email:\n")
    phone = input("Give me your phone:\n")
    csv["Id"][len(csv["Id"])] = len(csv["Id"])
    csv["Name"][len(csv["Name"])] = name
    csv["Email"][len(csv["Email"])] = email
    csv["Phone"][len(csv["Phone"])] = phone
    write = pd.DataFrame(csv)

    write.to_csv(CSV_URL, index=False)
    logger.info("CVS file updated")
    result = pd.read_csv(CSV_URL)
    logger.debug(result)
    return result


if __name__ == "__main__":
    logger = logging_console_file.logging_file("fund_module_6_retrieve_cvs")
    logger.info(" - - - - - - Start of the test - - - - - - ")

    cvs_data = load_cvs()
    cvs_write = write_csv(cvs_data)
    result = cvs_write[cvs_write["Id"] > 5]
    result = result.drop_duplicates(subset=["Name"])
    logger.debug("Without the duplicates, we have:")
    logger.debug(result)
