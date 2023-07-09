import logging
import logging.handlers
import os
import datetime

import requests

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
# formatter = logging.Formatter("%(message)s")
# logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)



if __name__ == "__main__":

    r = requests.get('https://jti-kelas-kosong.vercel.app/day/Selasa')
    if r.status_code == 200:
        
        # data = r.json()
        # print("\n")
        print(f'https://jti-kelas-kosong.vercel.app ping at : {datetime.datetime.now()}')

        logger.info(f'https://jti-kelas-kosong.vercel.app ping at : {datetime.datetime.now()}')