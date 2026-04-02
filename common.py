import logging
import os


def get_logger(name, level=logging.INFO):
    envLevel = os.getenv('COMFY_BOT_LOG_LEVEL', '').upper()
    levelMapping = {'CRITICAL': 50, 'FATAL': 50, 'ERROR': 40, 'WARN': 30, 'WARNING': 30, 'INFO': 20, 'DEBUG': 10, 'NOTSET': 0}
    if envLevel in levelMapping:
        level = levelMapping[envLevel]
    logger = logging.getLogger(name)
    c_handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s [%(levelname)s][%(name)s]: %(message)s')
    c_handler.setFormatter(formatter)
    logger.addHandler(c_handler)
    logger.setLevel(level)
    return logger
