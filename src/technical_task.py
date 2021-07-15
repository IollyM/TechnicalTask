import sys
import os
import string
import pandas as pd


def general():
    input_file_path = sys.argv[1]
    files_directory_path = sys.argv[2]
    if os.path.isfile(input_file_path):
        try:
            read_file(input_file_path, files_directory_path)
        except:
            print("Failed to read file")

    else:
        print('The path to the source file was entered incorrectly. '
              'The file was not found.')


def read_file(input_file_path, files_directory_path):
    file_reader = pd.read_csv(input_file_path, delim_whitespace='True', header=None)
    if file_reader.shape[1] != 3:
        print("Input file structure is incorrect")
    else:
        if os.path.isdir(files_directory_path):
            print(file_reader)
        # файл и сравнение хэшей
        else:
            print("The path to the  directory with files was entered incorrectly. "
                  "The directory was not found.")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f'Incorrect number of arguments entered. {len(sys.argv)} arguments were introduced, when 3 is needed. '
              f'(<your program> <path to the input file> <path to the directory containing the files to check>) ')
        sys.exit()
    else:
        general()
