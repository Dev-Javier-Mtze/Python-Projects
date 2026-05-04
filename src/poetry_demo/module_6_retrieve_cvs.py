import logging
import os
from typing import TypedDict

import pandas as pd
from logging_config import setup_logging

setup_logging()
logger = logging.getLogger("module_6_retrieve_cvs")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)
CSV_URL = f"{os.path.join(PROJECT_ROOT, 'poetry_demo/data', 'contact_list.csv')}"


class ContactList(TypedDict):
    Id: dict[int, int]
    Name: dict[int, str]
    Email: dict[int, str]
    Phone: dict[int, str]


def load_cvs() -> ContactList:
    result = pd.read_csv(CSV_URL)
    print(result)
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
    print(result)
    return result


cvs_data = load_cvs()
cvs_write = write_csv(cvs_data)
result = cvs_write[cvs_write["Id"] > 5]
result = result.drop_duplicates(subset=["Name"])
print(result)
