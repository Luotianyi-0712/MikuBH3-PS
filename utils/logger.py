import sys
from loguru import logger
from utils.config import Config

logger.remove()

LevelList = ["ERROR", "WARNING", "INFO", "DEBUG"]
CodeColorDict = {"ERROR": "red", "WARNING": "yellow", "INFO": "green", "DEBUG": "blue"}


def custom_format(record):
    color = CodeColorDict[record["level"].name]
    return f"<{color}>{record['level'].name}</{color}> : {record['message']}\n"


logger.add(sys.stdout, format=custom_format, colorize=True, level=Config.LogLevel)


def Log(msg, types):
    if types in CodeColorDict and LevelList.index(types) <= LevelList.index(
        Config.LogLevel
    ):
        getattr(logger, types.lower())(msg)


def Error(msg):
    Log(msg, "ERROR")


def Warn(msg):
    Log(msg, "WARNING")


def Info(msg):
    Log(msg, "INFO")


def Debug(msg):
    Log(msg, "DEBUG")
