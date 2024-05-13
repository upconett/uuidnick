from os import path
from json import dump, load


def valid_path(path: str) -> bool:
    try: open(path, 'r'); return True
    except: return False


def set_config(data: dict):
    with open(path.join(path.expanduser('~'), '.uuidnick'), 'a') as conf:
        dump(data, conf)


def first_start():
    whitelist_path = None

    print('Enter whitelist.json full path:')

    while not valid_path(whitelist_path):
        whitelist_path = input()
        if not valid_path(whitelist_path):
            print('The path is invalid, try again:')
    
    set_config({'whitelist_path': whitelist_path})
    print('Configuration complete\nRestart the tool')
    quit()


def get_config() -> dict:
    try:
        with open(path.join(path.expanduser('~'), '.uuidnick'), 'r') as conf:
            return load(conf)
    except:
        first_start()
        
