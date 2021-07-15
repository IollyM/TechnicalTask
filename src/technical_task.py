import sys
import os
import pandas as pd
import hashlib
from exceptions.custom import WrongPathError, \
    IncorrectArqQuantityError, UsedWrongHashError


def read_file(input_file_path):
    try:
        file_reader = pd.read_csv(
            input_file_path,
            delim_whitespace='True',
            header=None)
        return file_reader
    except UnicodeDecodeError:
        print("Change file to utf-8")
        sys.exit()
    except pd.errors.ParserError:
        print("Not csv format")
        sys.exit()


def encode_file(files_directory_path, filename, hash_type, hash):
    with open(os.path.join(files_directory_path, filename), "rb") as f:
        bytes = f.read()
        if hash_type == "md5":
            check_hash(hashlib.md5(bytes).hexdigest(), filename, hash)
        elif hash_type == "sha256":
            check_hash(hashlib.sha256(bytes).hexdigest(), filename, hash)
        elif hash_type == "sha1":
            check_hash(hashlib.sha1(bytes).hexdigest(), filename, hash)
        else:
            raise UsedWrongHashError(hash_type)


def check_hash(readable_hash, filename, hash):
    if readable_hash == hash:
        print(f'{filename} OK')
    else:
        print(f'{filename} FAIL')


def general(input_file_path, files_directory_path):
    if os.path.isfile(input_file_path):
        file_reader = read_file(input_file_path)
        if file_reader is None or file_reader.shape[1] != 3:
            raise TypeError("Input file structure is incorrect")
        else:
            if os.path.isdir(files_directory_path):
                for index, row in file_reader.iterrows():
                    if os.path.isfile(
                            os.path.join(files_directory_path, row[0])):
                        encode_file(
                            files_directory_path,
                            row[0],
                            row[1].lower(),
                            row[2]
                        )
                    else:
                        print(f'{row[0]} NOT FOUND')
            else:
                raise WrongPathError(
                    'to the  directory with files',
                    'directory'
                )
    else:
        raise WrongPathError('to the input file', 'file')


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise IncorrectArqQuantityError(len(sys.argv))
    else:
        general(sys.argv[1], sys.argv[2])
