import sys
import os
import pandas as pd
import hashlib
from exceptions.custom import WrongPathError, \
    IncorrectArqQuantityError, UsedWrongHashError


# Read file, check that it is possible to read the file


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


'''
Select the hash type, check that we can process it,
get the file hash and send it to the function for comparison.
'''


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


'''
Compare the hash of the file with the hash from the original file.
Display result information.
'''


def check_hash(readable_hash, filename, hash):
    if readable_hash == hash:
        print(f'{filename} OK')
    else:
        print(f'{filename} FAIL')


'''
A function that combines all steps into one sequence.
Checking the correctness of the file structure,
after checking the existence of a directory with files,
checking the existence of files from a file with input data.
Calling the function for calculating the hash of a file.
'''


def general(input_file_path, files_directory_path):
    if os.path.isfile(input_file_path):
        file_reader = read_file(input_file_path)
        if file_reader is None or file_reader.shape[1] != 3:
            raise TypeError("Input file structure is incorrect")
        else:
            if os.path.isdir(files_directory_path):
                for index, file_info in file_reader.iterrows():
                    if os.path.isfile(
                            os.path.join(files_directory_path, file_info[0])):
                        encode_file(
                            files_directory_path,
                            file_info[0],
                            file_info[1].lower(),
                            file_info[2]
                        )
                    else:
                        print(f'{file_info[0]} NOT FOUND')
            else:
                raise WrongPathError(
                    'to the  directory with files',
                    'directory'
                )
    else:
        raise WrongPathError('to the input file', 'file')


'''
Check that a valid number of arguments are entered
'''


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise IncorrectArqQuantityError(len(sys.argv))
    else:
        general(sys.argv[1], sys.argv[2])
