from datetime import datetime
from logging import FileHandler, StreamHandler
import logging
import os

data_hoje = datetime.today()
data_log = data_hoje.strftime("%Y_%m_%d")

os.makedirs("log", exist_ok=True)
pasta_log = os.path.join("log", f"log_{data_log}.log")

log_format = "%(asctime)s - %(levelname)s: %(message)s"
logging.basicConfig(
    format=log_format,
    level=logging.INFO,
    datefmt="%H:%M:%S",
    handlers=[FileHandler(pasta_log), StreamHandler()],
)

logging.debug("Esse é um log de DEBUG")
logging.info("Esse é um log de INFO")
logging.exception("Esse é um log de EXCEPTION")
logging.warning("Esse é um log de WARNING")
logging.critical("Esse é um log de CRITICAL")