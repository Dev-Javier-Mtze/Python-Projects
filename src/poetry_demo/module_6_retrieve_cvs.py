import logging

import pandas as pd

from logging_config import setup_logging

setup_logging()
logger = logging.getLogger("module_6_retrieve_cvs")


def load_cvs():
    result = pd.read_csv("./contact_list.csv")
    print(result)
    csv_dict = result.to_dict()
    return csv_dict


def write_csv(csv):
    name = input("Give me your name:\n")
    email = input("Give me your email:\n")
    phone = input("Give me your phone:\n")
    csv["Id"][len(csv["Id"])] = len(csv["Id"])
    csv["Name"][len(csv["Name"])] = name
    csv["Email"][len(csv["Email"])] = email
    csv["Phone"][len(csv["Phone"])] = phone
    print(csv)
    write = pd.DataFrame(csv)
    write.to_csv("./contact_list.csv", index=False)
    logger.info("CVS file updated")


cvs_data = load_cvs()
cvs_write = write_csv(cvs_data)
