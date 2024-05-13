from sys import argv
from json import load

from config import first_start


def get_uuid_nickname() -> tuple:
    uuid, nickname = (None, None)

    try: uuid_or_nickname = argv[1]
    except: return None, None

    if len(uuid_or_nickname) == 36 and uuid_or_nickname.count('-') == 4:
        uuid = uuid_or_nickname
    else:
        nickname = uuid_or_nickname
    return uuid, nickname


def get_whitelist(whitelist_path: str) -> list[dict]:
    with open(whitelist_path, 'r', encoding='utf-8') as file:
        return load(file)


def convert_uuid_to_nickname(whitelist_path: str, uuid: str) -> str:
    whitelist = get_whitelist(whitelist_path)
    for user in whitelist:
        if user['uuid'] == uuid:
            return user['name']
    else:
        return 'User with provided uuid is not in whitelist...'


def convert_nickname_to_uuid(whitelist_path: str, nickname: str) -> str:
    whitelist = get_whitelist(whitelist_path)
    for user in whitelist:
        if user['name'] == nickname:
            return user['uuid']
    else:
        return 'User with provided nickname is not in whitelist...'
    

def get_output_extension():
    try: return argv[2]
    except: return ''
