import json
import re
import time
from flask import Blueprint, Response, jsonify, request
from utils.aes import encrypt_ecb
from utils.config import Config

dispatch_blueprint = Blueprint("dispatch", __name__)


@dispatch_blueprint.route("/query_dispatch", methods=["GET"])
def query_dispatch():
    version = request.args.get("version")
    response_data = {
        "retcode": 0,
        "region_list": [
            {
                "retcode": 0,
                "dispatch_url": f"http://{Config.GameServer.IP}/query_gateway",
                "name": Config.RegionName,
                "title": "",
                "ext": get_ext(version),
            }
        ],
    }

    if Config.EnableDispatchEncryption:
        return Response(
            encrypt_ecb(Config.AESKeys.get(version), json.dumps(response_data)),
            mimetype="text/plain",
        )

    return jsonify(response_data)


@dispatch_blueprint.route("/query_gateway", methods=["GET"])
def query_gateway():
    version = request.args.get("version")
    gameserver = {"ip": Config.GameServer.IP, "port": Config.GameServer.Port}

    response_data = {
        "account_url": f"http://{Config.GameServer.IP}/account",
        "account_url_backup": f"http://{Config.GameServer.IP}/account",
        "asset_bundle_url_list": get_asset_bundle_url_list(version),
        # "ex_audio_and_video_url_list": get_ex_audio_and_video_url_list(version),
        "ex_resource_url_list": get_ex_resource_url_list(version),
        # TODO: Revisit this
        "ext": {
            "1058891250": "1",
            "1095990871": "1",
            "1245473982": "1",
            "1344653749": "0",
            "1360176971": "1",
            "1501014376": "1",
            "1744250417": "1",
            "1745366296": "2",
            "1839631329": "1",
            "1887219073": "1",
            "203732861": "1",
            "2110930505": "1",
            "308332524": "1",
            "763305743": "1",
        },
        "gameserver": gameserver,
        "gateway": gameserver,
        "is_data_ready": True,
        "manifest": {
            "Asb": {
                "android": {
                    "enable_time": 0.0,
                    "revision": "7.9.0.3",
                    "suffix": "32e095538f496ce873b84f7d800ad9fd",
                },
                "iphone": {
                    "enable_time": 0.0,
                    "revision": "7.9.0.3",
                    "suffix": "899786bb3ad18295da593e3a930e4d7c",
                },
                "pc": {
                    "enable_time": 0.0,
                    "revision": "7.9.0.3",
                    "suffix": "6bee17b8b2ffec47182c8c3c9aed21a9",
                },
            },
            "AsbPreDownload": {
                "android": {
                    "enable_time": 1730174400.0,
                    "encrypt_key": "298FC85F5988308213B6462562A3B095",
                    "revision": "7.9.0.0",
                    "suffix": "874af0171cec4d992537ed029906bc6e",
                },
                "iphone": {
                    "enable_time": 1730174400.0,
                    "encrypt_key": "298FC85F5988308213B6462562A3B095",
                    "revision": "7.9.0.0",
                    "suffix": "166391e65f2d4de973b1cd87d583a230",
                },
            },
            "Audio": {
                "platform": {
                    "Android": "manifest_2291f5be319191f1c1473e1c8abdd325.m",
                    "Windows": "manifest_b12c79d9ec59454e8695e049a4b2aa90.m",
                    "iOS": "manifest_6b1113eeaf6cd9e8b149efeeff64e4a9.m",
                },
                "revision": 727034,
            },
            "AudioPreDownload": {
                "enable_time": 1730174400,
                "platform": {
                    "Android": "manifest_74bc85237052ae2eba6a1937f90aa39e.m",
                    "Windows": "manifest_73a4b3611cff2b3bdd20405b8528e8f9.m",
                    "iOS": "manifest_5e3020c93eb651f8c8c25a87aea860f5.m",
                },
                "revision": 725668,
            },
            "VideoEncrypt": {
                "filename": "product_video_encrypt_0d89026956cc2bdd5714d4515f1d5df5"
            },
        },
        "msg": "",
        "oaserver_url": f"http://{Config.GameServer.IP}/oaserver",
        "region_name": Config.RegionName,
        "retcode": 0,
        "server_cur_time": int(time.time()),
        "server_cur_timezone": 8,
        "server_ext": {
            "cdkey_url": "http://127.0.0.1/common/",
            "is_official": "1",
            "mihoyo_sdk_env": "0",
            "use_account_web_url": "1",
        },
    }

    if Config.EnableDispatchEncryption:
        return Response(
            encrypt_ecb(Config.AESKeys.get(version), json.dumps(response_data)),
            mimetype="text/plain",
        )

    return jsonify(response_data)


def get_ext(version):
    return {
        "ai_use_asset_bundle": "0" if Config.UseLocalCache else "1",
        "apm_log_level": "0",
        "apm_log_dest": "2",
        "apm_switch": "0",
        "apm_switch_game_log": "1",
        "apm_switch_crash": "1",
        "block_error_dialog": "1",
        "elevator_model_path": "GameEntry/EVA/StartLoading_Model",
        "data_use_asset_bundle": "1",
        "enable_watermark": "1",
        "ex_audio_and_video_url_list": get_ex_audio_and_video_url_list(version),
        "ex_res_buff_size": "10485760",
        "ex_res_pre_publish": "0",
        "ex_res_use_http": "1",
        "ex_resource_url_list": get_ex_resource_url_list(version),
        "is_xxxx": "0",
        "mtp_switch": "0",
        "network_feedback_enable": "0",
        "offline_report_switch": "0",
        "forbid_recharge": "1",
        "is_checksum_off": "0" if Config.UseLocalCache else "1",
        "res_use_asset_bundle": "1",
        "show_version_text": "0",
        "update_streaming_asb": "0",
        "use_multy_cdn": "1",
        "show_bulletin_button": "1",
        "show_bulletin_empty_dialog_bg": "0",
    }


def get_asset_bundle_url_list(version):
    # Compile the regex pattern
    regex = re.compile(r"^(.*?)_(os|gf|global)_(.*?)$")
    match = regex.match(version)
    value = match.group(2)
    if Config.UseLocalCache:
        return get_local_url_list(value, version)
    # Proceed if there's a match
    if match:
        # Return URLs based on the OS type
        if value == "os":
            return [
                "https://bundle-aliyun-os.honkaiimpact3.com/asset_bundle/overseas01/1.1",
                "https://hk-bundle-os-mihayo.akamaized.net/asset_bundle/overseas01/1.1",
            ]
        elif value == "gf":
            if "beta" in version:
                return [
                    "https://autopatchbeta.bh3.com/asset_bundle/beta_release/1.0",
                    "https://autopatchbeta.bh3.com/asset_bundle/beta_release/1.0",
                ]
            return [
                "https://bundle-qcloud.bh3.com/asset_bundle/android01/1.0",
                "https://bundle.bh3.com/asset_bundle/android01/1.0",
            ]
        elif value == "global":
            return [
                "http://hk-bundle-west-mihayo.akamaized.net/asset_bundle/usa01/1.1",
                "http://bundle-aliyun-usa.honkaiimpact3.com/asset_bundle/usa01/1.1",
            ]
        else:
            return [
                "https://bundle-aliyun-os.honkaiimpact3.com/asset_bundle/overseas01/1.1",
                "https://hk-bundle-os-mihayo.akamaized.net/asset_bundle/overseas01/1.1",
            ]
    return []


def get_ex_audio_and_video_url_list(version):
    # Compile the regex pattern
    regex = re.compile(r"^(.*?)_(os|gf|global)_(.*?)$")
    match = regex.match(version)
    value = match.group(2)
    if Config.UseLocalCache:
        return get_local_url_list(value, version)
    if match:
        # Return URLs based on the OS type
        if value == "os":
            return [
                "bigfile-aliyun-os.honkaiimpact3.com/com.miHoYo.bh3oversea",
                "hk-bigfile-os-mihayo.akamaized.net/com.miHoYo.bh3oversea",
            ]
        elif value == "gf":
            if "beta" in version:
                return [
                    "autopatchbeta.bh3.com/tmp/CGAudio",
                    "autopatchbeta.bh3.com/tmp/CGAudio",
                ]
            return [
                "bh3rd-beta-qcloud.bh3.com/tmp/CGAudio",
                "bh3rd-beta.bh3.com/tmp/CGAudio",
            ]
        elif value == "global":
            return [
                "bh3rd-beta-qcloud.bh3.com/tmp/CGAudio",
                "bh3rd-beta.bh3.com/tmp/CGAudio",
            ]
        else:
            return [
                "bh3rd-beta-qcloud.bh3.com/tmp/CGAudio",
                "bh3rd-beta.bh3.com/tmp/CGAudio",
            ]
    return []


def get_ex_resource_url_list(version):
    # Compile the regex pattern
    regex = re.compile(r"^(.*?)_(os|gf|global)_(.*?)$")
    match = regex.match(version)
    value = match.group(2)
    if Config.UseLocalCache:
        return get_local_url_list(value, version)
    # Proceed if there's a match
    if match:
        # Return URLs based on the OS type
        if value == "os":
            return [
                "bigfile-aliyun-os.honkaiimpact3.com/com.miHoYo.bh3oversea",
                "hk-bigfile-os-mihayo.akamaized.net/com.miHoYo.bh3oversea",
            ]
        elif value == "gf":
            if "beta" in version:
                return [
                    "autopatchbeta.bh3.com/tmp/beta",
                    "autopatchbeta.bh3.com/tmp/beta",
                ]
            return ["bundle-qcloud.bh3.com/tmp/Original", "bundle.bh3.com/tmp/Original"]
        elif value == "global":
            return [
                "hk-bundle-west-mihayo.akamaized.net/tmp/com.miHoYo.bh3global",
                "bigfile-aliyun-usa.honkaiimpact3.com/tmp/com.miHoYo.bh3global",
            ]
        else:
            return [
                "bigfile-aliyun-os.honkaiimpact3.com/com.miHoYo.bh3oversea",
                "hk-bigfile-os-mihayo.akamaized.net/com.miHoYo.bh3oversea",
            ]
    return []


def get_local_url_list(type, version):
    return [
        f"http://{Config.GameServer.IP}/statics/{type}/{version.replace('.', '_')}",
        f"http://{Config.GameServer.IP}/statics/{type}/{version.replace('.', '_')}",
    ]
