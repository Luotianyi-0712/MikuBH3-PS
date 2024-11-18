import betterproto
from utils.time import get_unix_in_seconds
from game_server.net.session import Session
from game_server.game.chat.command_handler import handler
from lib.proto import (
    SendChatMsgNotify,
    RecvChatMsgNotify,
    ChatMsg,
    ChatMsgSensitiveCheckResult,
    ChatMsgMsgChannel,
    ChatMsgContent,
    ChatMsgItem
)


async def handle(session: Session, msg: SendChatMsgNotify) -> betterproto.Message:
    string_msg=[msg.msg_str for msg in msg.chat_msg.content.items if msg.msg_str != None][0]
    msgs=[
        ChatMsg(
            uid=session.player.uid,
            nickname=session.player.name,
            time=get_unix_in_seconds(),
            msg=string_msg,
            channel=ChatMsgMsgChannel.WORLD.value,
            avatar_id=session.player.assistant_avatar_id,
            dress_id=session.player.avatars.get(session.player.assistant_avatar_id).dress_id,
            frame_id=session.player.head_frame,
            custom_head_id=session.player.head_photo,
            check_result=ChatMsgSensitiveCheckResult(
                rewrite_text=string_msg
            ),
            content=ChatMsgContent(
                items=[
                    ChatMsgItem(
                        msg_str=string_msg
                    )
                ]
            )
        )
    ]
    text = await handler.handle_command(session, string_msg)
    if text:
        msgs.append(
            ChatMsg(
                uid=0,
                nickname="Ai-Chan",
                time=get_unix_in_seconds(),
                msg=text,
                channel=ChatMsgMsgChannel.WORLD.value,
                avatar_id=3201,
                dress_id=593201,
                frame_id=200001,
                custom_head_id=161080,
                check_result=ChatMsgSensitiveCheckResult(
                    rewrite_text=text
                ),
                content=ChatMsgContent(
                    items=[
                        ChatMsgItem(
                            msg_str=text
                        )
                    ]
                )
            )
        )
    return RecvChatMsgNotify(
        chat_msg_list=msgs
    )
