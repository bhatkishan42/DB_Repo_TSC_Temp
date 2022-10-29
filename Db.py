# Creating the base Db file for practice.

import pandas as pd
import MySQLdb
import os

from dotenv import load_dotenv, find_dotenv #loading the env file

load_dotenv(find_dotenv())

user = os.environ.get("user")
passwd = os.environ.get("password")
print(user, passwd)




