#!/usr/bin/env python3

import hashlib
import pathlib
import pickle

REPO_ROOT = pathlib.Path(__file__).parent
TARGETS_PICKLE = REPO_ROOT / 'targets.pickle'


def main():
    cookie = get_cookie()
    stack_goal = (0x0000_7fff_ffff_0000 - cookie).to_bytes(8, 'little')

    with open(TARGETS_PICKLE, 'rb') as file:
        targets: list[tuple[str, int, bytes]] = pickle.load(file)

    for target_name, target_offset, target_bin in targets:
        target_output = REPO_ROOT / target_name

        target_bin = bytearray(target_bin)
        target_bin[target_offset:target_offset + 8] = stack_goal
        target_output.write_bytes(target_bin)


def get_cookie() -> int:
    cookie_file = REPO_ROOT / 'cookie'

    try:
        cookie_file_contents = cookie_file.read_text()
        uniqname_line = cookie_file_contents.split('\n')[0]
    except FileNotFoundError:
        cookie_file_contents = None
        print('Enter the uniqnames of all members of your team, separated by spaces. Each group\'s targets will be slightly different, so make sure your uniqnames are correct!\n')
        uniqname_line = input('Enter uniqnames separated by spaces: ')

    uniqnames = sorted(list(set(uniqname_line.rstrip().casefold().split())))
    print(f'Using cookie for {uniqnames}')
    cookie = int.from_bytes(hashlib.sha256(
        ('|'.join(uniqnames)).encode()).digest(), byteorder='little') % 0x7FFF

    expected_cookie_file_contents = f'{" ".join(uniqnames)}\n{cookie}\n'
    if cookie_file_contents is None:
        cookie_file.write_text(expected_cookie_file_contents)
    elif cookie_file_contents.rstrip() != expected_cookie_file_contents.rstrip():
        raise Exception(
            'The cookie file is malformed. Try deleting it and trying again.'
        )

    return cookie


if __name__ == '__main__':
    main()
