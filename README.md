# TechnicalTask

## О программе

Задание
```
Дан файл, содержащий имена файлов, алгоритм хэширования (один из MD5/SHA1/SHA256) и соответствующие им хэш-суммы, вычисленные по соответствующему алгоритму и указанные в файле через пробел. Напишите программу, читающую данный файл и проверяющую целостность файлов.
Пример
Файл сумм:
file_01.bin md5 aaeab83fcc93cd3ab003fa8bfd8d8906
file_02.bin md5 6dc2d05c8374293fe20bc4c22c236e2e
file_03.bin md5 6dc2d05c8374293fe20bc4c22c236e2e
file_04.txt sha1 da39a3ee5e6b4b0d3255bfef95601890afd80709
Пример вызова:  
<your program> <path to the input file> <path to the directory containing the files to check>
Формат вывода:
file_01.bin OK
file_02.bin FAIL
file_03.bin NOT FOUND
file_04.txt OK
```

Реализовано на языке программирования Python 3.8 c использованием библиотек pandas, hashlib.
## Установка

Для того чтобы установить программу необходимо, наличие на компьютере Python 3, системы управлением пакетами pip.
После этого необходимо установить зависимости, запустив из директории проекта следующую команду.

    pip install -e .

## Запуск

При запуске программы из директории с иходным кодом необходимо указать следующие параметры:
+ your program - имя файла программы ;
+ path to the input file - путь до файла с входными данными;
+ path to the directory containing the files to check - путь до директории с файлами.

Пример запуска на Windows OS.(python3 ecли у вас интерпретатором по умолчанию  является python версии 2)

    python technical_task.py C:\path\to\input\file C:\path\to\files\directory

Пример запуска на Linux.(python3 ecли у вас интерпретатором по умолчанию  является python версии 2)
    
    python technical_task.py /path/to/input/file /path/to/files/directory

## Дополнительная информация

В программе используются следующие оповещения и исключения:
+ "Change file to utf-8" - не удалось прочесть файл с вводными данными из-за проблем с кодировкой;
+ "Not csv format" - файл, не обладает необходимым форматом;
+ "Incorrect number of arguments entered. ... arguments were introduced, when 3 is needed..."  - программа запущена с неверным количеством аргументов;
+ "The path ... was entered incorrectly. ... was not found" - путь введен некорректно, либо файл не найден, либо директория с файлами;
+ "... is an invalid hash function. Use md5,sha1,sha256" - в исходном файле указан алгоритм, который не реализован в программе;
+ "Input file structure is incorrect" - в файле указано отличное от примера количество колонок.

