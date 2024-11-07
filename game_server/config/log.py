import json
import sys
from loguru import logger

# Configuration for the logger
logger.remove()
with open("Config.json", "r", encoding="utf-8") as f:
    LogLevel = json.load(f)["LogLevel"]
LevelList = ["ERROR", "WARNING", "INFO", "DEBUG"]
CodeColorDict = {
    "ERROR": "red",
    "WARNING": "yellow",
    "INFO": "green",
    "DEBUG": "blue"
}

def custom_format(record):
    color = CodeColorDict[record["level"].name]
    return f"<{color}>{record['level'].name}</{color}> : {record['message']}\n"

logger.add(sys.stdout, format=custom_format, colorize=True, level=LogLevel)

def Log(msg, types):
    if types in CodeColorDict and LevelList.index(types) <= LevelList.index(LogLevel):
        getattr(logger, types.lower())(msg)

def Error(msg):
    Log(msg, "ERROR")

def Warn(msg):
    Log(msg, "WARNING")

def Info(msg):
    Log(msg, "INFO")

def Debug(msg):
    Log(msg, "DEBUG")
