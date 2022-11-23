from sys import stderr

class Logger:
    def __init__(self, verbosity: bool = False):
        # foreground code
        self.verbosity = verbosity
        self.__green = '\033[0;32m'
        self.__red = '\033[0;31m'
        self.__yellow = '\033[1;33m'
        self.__white = '\033[1;97'
        self.__end_color = '\033[0m'
    
    def set_verbosity(self, verbosity: bool):
        self.verbosity = verbosity
    
    def log(self, message: str):
        if self.verbosity:
            print(f'> {self.__green}{message}{self.__end_color}')
    
    def warn(self, message, file=stderr):
        print(f'{self.__yellow} WARNING: {message}{self.__end_color}', file=file)
    
    def error(self, message, file= stderr):
        print(f'{self.__red} ERROR: {message}{self.__end_color}', file=file)

