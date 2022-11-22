# from sys import argv
import argparse
from pathlib import Path
from sys import stderr
from libs.CpError import CpError

def dump(src: Path, dest: Path):
    with open(src, 'rb') as s, open(dest, 'wb') as d:
        d.write(s.read())

def copy_directory(src: str, dest: str, override: bool = False):
    print('cp dir')

def copy_file(src: str, dest: str, override: bool = False):
    if dest.is_dir():
        dest = dest / src.name
    if dest.is_file() and not override:
        raise CpError(f'Cannot override {dest}, specify -o option')
    print(f'Copy: {src} -> {dest}')
    dest.touch()
    dump(src, dest)
    

def copy(src: Path, dest: Path, override: bool= False):
    if src.is_file():
        copy_file(src, dest, override)
    elif src.is_dir():
        dest_is_dir = dest.is_dir()
        if not dest_is_dir and dest.exists():
            raise CpError(f'Destination {dest} is not a directory')
        copy_directory(src, dest, override)
    else:
        raise CpError('file type not supported')

def cli() -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog= 'cp', description= 'cp command implementation in python')
    parser.add_argument('-o', '--override', action='store_true', help='Override destination files if they already exist')
    parser.add_argument('-r', '--recursive', action='store_true', help='Copy directories recursively')
    parser.add_argument('source', help= 'source directory or file', type= Path)
    parser.add_argument('destination', help= 'destination directory or file', type= Path)
    return parser.parse_args()

def main():
    try:
        args = cli()
        copy(args.source, args.destination, args.override)
    except CpError as ex:
        print(ex, file=stderr) #imprime el error
        exit(1)



if __name__ == '__main__':
    main()



