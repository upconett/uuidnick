from config import get_config
from converter import *



if __name__ == '__main__':
    whitelist_path = get_config()['whitelist_path']
    extension = get_output_extension()
    uuid, nickname = get_uuid_nickname(extension)

    if nickname in ['--help', '-h']: nickname = None
    if uuid:
        print(convert_uuid_to_nickname(whitelist_path, uuid, extension))
    elif nickname:
        print(convert_nickname_to_uuid(whitelist_path, nickname, extension))
    else:
        print()
        print(
            'No uuid or nickname provided! \n\n'
            'This tool converts Minecraft UUID to nickname and vice versa \n'
            'It uses data from your server whitelist.json \n\n'
            'Usage: uuidnick <uuid or nickname> <file extension (if needed)>'
        )
        print()
