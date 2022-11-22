# from sys import argv
import argparse
from pathlib import Path
from sys import stderr
from libs.cp_error import CpError
from libs.logger import Logger

logger = Logger()

def dump(src: Path, dest: Path):
    with open(src, 'rb') as s, open(dest, 'wb') as d:
        d.write(s.read())

def copy_directory(src_dir: Path, dest_dir: Path, override: bool = False):
    for src_child in src_dir.iterdir():
        dest_child = dest_dir / src_child.name
        if src_child.is_dir():
            logger.log(f'Copy [dir] {src_child} -> {dest_child}')
            dest_child.mkdir(exist_ok=True)
            copy_directory(src_child, dest_child, override)
        elif src_child.is_file():
            if dest_child.is_file() and not override:
                logger.warn(f'Skipping {src_child} -> {dest_child} as -o is not present')
            else:
                logger.log(f'Copy [file] {src_child} -> {dest_child}')
                dest_child.touch()
                dump(src_child, dest_child)
        else:
            logger.error(f'Skipping {src_child} because file type is not supported')


def copy_file(src: str, dest: str, override: bool = False):
    if dest.is_dir():
        dest = dest / src.name
    if dest.is_file() and not override:
        raise CpError(f'Cannot override {dest}, specify -o option')
    logger.log(f'Copy: {src} -> {dest}')
    dest.touch()
    dump(src, dest)
    

def copy(src: Path, dest: Path, override: bool= False, recursive: bool = False):
    if src.is_file():
        copy_file(src, dest, override)
    elif src.is_dir():
        dest_is_dir = dest.is_dir()
        if not dest_is_dir and dest.exists():
            raise CpError(f'Destination {dest} is not a directory')
        if not recursive:
            raise CpError(f'Skipping directory {src} because -r not present')
        if dest_is_dir:
            dest = dest / src.name
        dest.mkdir(exist_ok=True)
        copy_directory(src, dest, override)
    else:
        raise CpError('file type not supported')

def cli() -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog= 'cp', description= 'cp command implementation in python')
    parser.add_argument('-o', '--override', action='store_true', help='Override destination files if they already exist')
    parser.add_argument('-r', '--recursive', action='store_true', help='Copy directories recursively')
    parser.add_argument('-v', '--verbose', action='store_true', help='Give details about actions being performed')
    parser.add_argument('-i', '--interactive', action='store_true', help='Give details about actions being performed')
    parser.add_argument('source', help= 'source directory or file', type= Path)
    parser.add_argument('destination', help= 'destination directory or file', type= Path)
    return parser.parse_args()

def main():
    try:
        args = cli()
        logger.set_verbosity(args.verbose)
        copy(args.source, args.destination, args.override, args.recursive)
    except CpError as ex:
        logger.error(ex)
        exit(1)



if __name__ == '__main__':
    main()



