import importlib
import os
import sys


folder = "game_server/game/chat/command"
sys.path.append(os.path.dirname(folder))

for filename in os.listdir(folder):
    if filename.endswith(".py") and filename != "__init__.py":
        module_name = filename[:-3]
        module_path = f"game_server.game.chat.command.{module_name}"
        try:
            importlib.import_module(module_path)
        except Exception as e:
            print(f"Error importing module '{module_path}': {e}")
