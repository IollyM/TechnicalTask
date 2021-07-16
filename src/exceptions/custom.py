'''
Explanatory exceptions that indicate errors were made in use.
'''


class IncorrectArqQuantityError(Exception):
    def __init__(self, quantity):
        message = f'Incorrect number of arguments entered. ' \
                  f'{quantity} arguments were introduced,' \
                  f' when 3 is needed. ' \
                  f'(<your program> <path to the input file>' \
                  f' <path to the directory containing the files to check>) '
        super().__init__(message)


class WrongPathError(Exception):
    def __init__(self, part1, part2):
        message = f'The path {part1} was entered incorrectly.' \
                  f' The {part2} was not found.'
        super().__init__(message)


class UsedWrongHashError(Exception):
    def __init__(self, hash):
        message = f'{hash} is an invalid hash function. Use md5,sha1,sha256'
        super().__init__(message)
