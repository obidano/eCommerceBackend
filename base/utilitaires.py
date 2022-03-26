import logging
import os
import sys
import traceback


def createFolders(list_path):
    for path in list_path:
        if not os.path.isdir(path):
            os.mkdir(path)


def createSQLiteFile(base_dir):
    sqlite_path=os.path.join(base_dir, 'db.sqlite3')
    if not os.path.isfile(sqlite_path):
        with open(sqlite_path, 'w') as fp:
            pass


def configDebugLog(type, path):
    from datetime import datetime
    LOGS_LEVEL = dict(debug=logging.DEBUG, info=logging.INFO,
                      error=logging.ERROR, ws=logging.DEBUG, ws_error=logging.ERROR)

    log_level = LOGS_LEVEL.get(type, 'debug')
    # create logger
    if type == 'error':
        logger = logging.getLogger("error")
        log_format = '%(levelname)s %(asctime)s %(module)s:%(funcName)s line:%(lineno)d \n\t\t%(message)s'
    else:
        log_format = '%(levelname)s %(asctime)s %(module)s:%(funcName)s line:%(lineno)d %(message)s'
        logger = logging.getLogger("debug")

    logger.setLevel(log_level)
    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(log_level)
    formatter = logging.Formatter(log_format)
    ch.setFormatter(formatter)
    logger.propagate = True
    datenow = str(datetime.now().date())

    log_path = path % datenow
    fileh = logging.FileHandler(filename=log_path)
    fileh.setFormatter(formatter)
    logger.addHandler(fileh)

    return logger
