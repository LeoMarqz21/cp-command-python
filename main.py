# from sys import argv
import argparse
from pathlib import Path
from sys import stderr
from libs.CpError import CpError

def copy_directory(src: str, dest: str):
    print('cp dir')

def copy_file(src: str, dest: str):
    if dest.is_dir():
        dest = dest / src.name
    if dest.is_file():
        raise CpError(f'Cannot override {dest}')
    print(f'Copy: {src} -> {dest}')
    

def copy(src: Path, dest: Path):
    if src.is_file():
        copy_file(src, dest)
    elif src.is_dir():
        copy_directory(src, dest)
    else:
        raise CpError('file type not supported')

def cli() -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog= 'cp', description= 'cp command implementation in python')
    parser.add_argument('source', help= 'source directory or file', type= Path)
    parser.add_argument('destination', help= 'destination directory or file', type= Path)
    return parser.parse_args()

def main():
    try:
        args = cli()
        copy(args.source, args.destination)
    except CpError as ex:
        print(ex, file=stderr) #imprime el error
        exit(1)



if __name__ == '__main__':
    main()



