from utils.logger import Info
from game_server.game.chat.decorators import command_registry
from game_server.net.session import Session
import game_server.game.chat.command  # noqa: F401


class CommandHandler:
    def load_commands(self):
        registered_commands = ", ".join(
            item.prefix for item in command_registry.values() if not item.is_alias
        )

        Info(
            f"[BOOT] [CommandHandler] Registered {len(command_registry)} game commands => {registered_commands}"
        )

    def parse_command(self, content: str):
        content = content.lstrip("/")
        parts = content.split(maxsplit=1)
        if len(parts) < 2:
            return parts[0], ""

        return parts[0], parts[1]

    def print_help(self):
        result = "Available commands:\n"
        for index, (_, func) in enumerate(command_registry.items()):
            result += f"{index+1}) {func.usage}\n\n"
        return result

    async def handle_command(self, session: Session, content: str):
        if content == "/help":
            return self.print_help()

        command_label, args = self.parse_command(content)
        command_func = command_registry.get(command_label)

        if command_func is not None:
            func_args_cnt = command_func.__code__.co_argcount - 1
            args_list = args.split()[:func_args_cnt]

            if args_list and args_list[0] == "help":
                return f"Usage: {command_func.usage}"

            try:
                return await command_func(session, *args_list)
            except TypeError:
                return f"Usage: {command_func.usage}"

        return None


handler = CommandHandler()
