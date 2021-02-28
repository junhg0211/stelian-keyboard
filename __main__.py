from datetime import datetime

from keyboard import add_abbreviation, wait
from json import load, dump


def register(key, value, *args, **kwargs):
    add_abbreviation(key, value, *args, **kwargs)
    print(f'{datetime.now()}\t{key} → {value}')


def main():
    with open('./res/abbreviations.json', 'r', encoding='utf-8') as file:
        data = load(file)
    for key, value in data.items():
        if value.upper() != value:
            register(key.upper(), value.upper(), match_suffix=True)
        register(key, value, match_suffix=True)
    with open('./res/abbreviations.json', 'w', encoding='utf-8') as file:
        dump(data, file, indent=4, ensure_ascii=False)
    wait()


if __name__ == '__main__':
    main()
