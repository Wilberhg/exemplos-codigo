# from dotenv import load_dotenv
# import os
# from sqlalchemy.engine import URL
# import pyodbc

# load_dotenv()

# SQLALCHEMY_DATABASE_URL = URL.create(
#     drivername="mssql+pyodbc",
#     username=os.environ.get("DB_USER"),
#     password=os.environ.get("DB_PASSWORD"),
#     host=os.environ.get("DB_SERVER"),
#     port=1433,
#     database=os.environ.get("DB_BASE"),
#     query={
#         "driver": [
#             driver for driver in pyodbc.drivers() if driver.endswith("SQL Server")
#         ][-1]
#     },
# )

SQLALCHEMY_DATABASE_URL = "sqlite:///./demo_challenge.db"
