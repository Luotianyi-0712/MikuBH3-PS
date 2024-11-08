from enum import Enum
import logging
from pathlib import Path

from flask import Flask, send_from_directory
from sdk_server.controllers.account_controller import account_blueprint
from sdk_server.controllers.config_controller import config_blueprint
from sdk_server.controllers.dispatch_controller import dispatch_blueprint
from utils.logger import Info


class VerboseLevel(Enum):
    SILENT = 0
    NORMAL = 1
    DEBUG = 2


class RequestLoggingMiddleware:
    suppressed_routes = ["/report", "/sdk/dataUpload"]

    def __init__(self, app, verbose_level):
        self.app = app
        self.verbose_level = verbose_level

    def __call__(self, environ, start_response):
        path = environ.get("PATH_INFO", "")
        method = environ.get("REQUEST_METHOD", "").upper()

        def custom_start_response(status, headers, *args):
            status_code = int(status.split()[0])

            if self.verbose_level.value > VerboseLevel.NORMAL.value:
                Info(f"{status_code} {method} {path}")
            elif (
                self.verbose_level.value > VerboseLevel.SILENT.value
                and path not in self.suppressed_routes
            ):
                Info(f"{status_code} {method} {path}")

            return start_response(status, headers, *args)

        return self.app(environ, custom_start_response)


app = Flask(__name__)


app.wsgi_app = RequestLoggingMiddleware(app.wsgi_app, verbose_level=VerboseLevel.NORMAL)


resources_path = Path(__file__).resolve().parent.parent / "resources/statics"
if not resources_path.exists():
    resources_path.mkdir(parents=True)


@app.route("/statics/<path:filename>")
def serve_statics(filename):
    return send_from_directory(resources_path, filename)


app.register_blueprint(account_blueprint)
app.register_blueprint(config_blueprint)
app.register_blueprint(dispatch_blueprint)


def HandleSdkServer(ServerIp, GameServerPort, SdkServerPort):
    app.config["SERVER_IP"] = ServerIp
    app.config["GAME_SERVER_PORT"] = GameServerPort

    log = logging.getLogger("werkzeug")
    log.setLevel(logging.ERROR)

    Info(f"HTTP server started on port {SdkServerPort}")

    app.run(host=ServerIp, port=SdkServerPort)


def HandleSslSdkServer():
    log = logging.getLogger("werkzeug")
    log.setLevel(logging.ERROR)
    Info("HTTPS server started on port 443")
    app.run(host="127.0.0.1", port=443, ssl_context="adhoc")
