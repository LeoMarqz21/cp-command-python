# from sys import argv
import argparse
from pathlib import Path

def copy_directory(src: str, dest: str):
    pass

def copy_file(src: str, dest: str):
    pass

def copy(src: Path, dest: Path):
    print('path: source -> ' , src.absolute())
    print('path: destination -> ' , dest.absolute())

def cli() -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog= 'cp', description= 'cp command implementation in python')
    parser.add_argument('source', help= 'source directory or file', type= Path)
    parser.add_argument('destination', help= 'destination directory or file', type= Path)
    return parser.parse_args()

def main():
    args = cli()
    copy(args.source, args.destination)



if __name__ == '__main__':
    main()



